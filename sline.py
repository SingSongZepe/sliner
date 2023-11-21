import typing

from sline_ui import Ui_MainWindow
from value.strings import *
from value.value import *
from value.pic import *
from object.mode import Mode
from object.point import PointF
from object.stack import UndoStack, RedoStack
from object.graphics import GraphicsPoints, GraphicsLines
from object.selected_graphics_objects import SelectedGraphicsObjects
from object.selected_graphics_item import SelectedGraphicsItem
from object.assist_graphics_item import AssistGraphicsItem
from object.selected_events import SelectedEvents
from utils.common.log import *

from PySide6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QGraphicsItem
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import QMutex, Qt

class SLINE(QMainWindow, Ui_MainWindow):

    # ! sline functions
    from sline_functions.mouse_click import mouse_click
    from sline_functions.mouse_move import mouse_move
    from sline_functions.key_press import key_press
    from sline_functions.mouse_double_click import mouse_double_click
    from sline_functions.wheel_roll import wheel_roll
    from sline_functions.mouse_release import mouse_release

    # ! utils
    from utils.sline.toggle_mode import toggle_mode

    # ! draw
        # real
    from draw.real.draw_point import draw_point
    from draw.real.draw_line import draw_line
    from draw.real.draw_rect import draw_rect
    from draw.real.draw_text import draw_vertical, draw_horizontal, draw_perpendicular, draw_parallel ,draw_line_info
        # assist
    from draw.assist.draw_assist_line import draw_assist_line
    from draw.assist.draw_assist_point import draw_assist_point
    from draw.assist.draw_assist_rect import draw_assist_rect
    from draw.assist.draw_assist_text import draw_assist_vertical, draw_assist_horizontal, draw_assist_perpendicular, draw_assist_parallel, draw_assist_line_info

    # ! constrain
    from constrain.point.constrain_point import constrain_point
    from constrain.line.constrain_line import constrain_line

    # ! select
        # select
    from select_.point.select_point import select_point
    from select_.line.select_line import select_line
        # unselect
    from select_.unselect import unselect

    # ! functions
    from functions.delete_event import delete_event
    from functions.change_color import change_to_selected, change_to_default
    from functions.clear_assist import clear_assist
    from functions.undo import undo
    from functions.redo import redo
    
    # ! process
    from process.point.process_point import process_point
    from process.point.process_assist_point import process_assist_point
    from process.line.process_line import process_line
    from process.line.process_assist_line import process_assist_line
    from process.trim.process_trim import process_trim

    # ! indicator
    from indicator.indicate_mouse_pos import indicate_mouse_pos

    def __init__(self) -> None:
        super(SLINE, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title_main)
        self.setWindowIcon(QPixmap(pic_path_sszp))

        # icon
        self.lb_emp.setPixmap(QPixmap(pic_path_emp))
        self.lb_point.setPixmap(QPixmap(pic_path_point))
        self.lb_line.setPixmap(QPixmap(pic_path_line))
        self.lb_arc.setPixmap(QPixmap(pic_path_arc_by_center))
        self.lb_trim.setPixmap(QPixmap(pic_path_trim))
        self.lb_delete.setPixmap(QPixmap(pic_path_delete))

        # graphics
        self.gv_graphics = QGraphicsView()
        self.gs_graphics = QGraphicsScene()
        self.gv_graphics.setScene(self.gs_graphics)
        self.vl_gv = QVBoxLayout(self.wgt_graphics)
        self.vl_gv.addWidget(self.gv_graphics)

        # optional setting
        # if don't open this option, then only press and toggle mouse can trigger mouseMoveEvent
        self.gv_graphics.setMouseTracking(True)
        # self.gv_graphics.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # self.gv_graphics.setDragMode(QGraphicsView.ScrollHandDrag)

        self.gv_graphics.setRenderHint(QPainter.Antialiasing)
        self.gv_graphics.setSceneRect(self.gv_graphics.rect())
        # ! click important + translate
        self.gv_graphics.mousePressEvent = self.mouse_click
        # ! key shortcut
        self.gv_graphics.keyPressEvent = self.key_press
        # ! mouse move assist
        self.gv_graphics.mouseMoveEvent = self.mouse_move
        # ! select object
        self.gv_graphics.mouseDoubleClickEvent = self.mouse_double_click
        # ! for scaling translating
        self.gv_graphics.wheelEvent = self.wheel_roll
        # ! for translating
        self.gv_graphics.mouseReleaseEvent = self.mouse_release

        # label event
        self.lb_emp.setCursor(Qt.CursorShape.PointingHandCursor)
        self.lb_emp.mousePressEvent = lambda _: self.toggle_mode(Mode.Emp)
        self.lb_point.setCursor(Qt.CursorShape.PointingHandCursor)
        self.lb_point.mousePressEvent = lambda _: self.toggle_mode(Mode.Point)
        self.lb_line.setCursor(Qt.CursorShape.PointingHandCursor)
        self.lb_line.mousePressEvent = lambda _: self.toggle_mode(Mode.Line)
        self.lb_arc.setCursor(Qt.CursorShape.PointingHandCursor)
        self.lb_arc.mousePressEvent = lambda _: self.toggle_mode(Mode.Arc)
        self.lb_trim.setCursor(Qt.CursorShape.PointingHandCursor)
        self.lb_trim.mousePressEvent = lambda _: self.toggle_mode(Mode.Trim)
        self.lb_delete.setCursor(Qt.CursorShape.PointingHandCursor)
        self.lb_delete.mousePressEvent = lambda _: self.toggle_mode(Mode.Delete)
        
        # data init
        self.__other_init__()
    
    def __other_init__(self) -> None:
        self.mutex = QMutex()

        # undo and redo stack
        self.undo_stack = UndoStack()
        self.redo_stack = RedoStack()

        self.graphics_points = GraphicsPoints()
        self.graphics_lines = GraphicsLines()

        self.selected_graphics_object = SelectedGraphicsObjects()
        self.selected_graphics_item = SelectedGraphicsItem()

        # assist
        self.assist_graphics_item = AssistGraphicsItem()

        # selected
        self.selected_events = SelectedEvents()

        # flag for translating
        self._tran = False
        self._tran_start_pos: PointF = None
        
        # flag for rect select
        self._rect_select = False
        self._rect_select_start_pos: PointF = None

        # default mode
        self.mode = Mode.Emp

        ln('Sliner init successfully')


