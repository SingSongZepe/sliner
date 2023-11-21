import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from value.strings import *
from value.value import *

from PySide6.QtWidgets import QGraphicsTextItem
from PySide6.QtCore import QPointF, QRectF, QPoint
from PySide6.QtGui import QFontMetrics, QFont

def draw_horizontal(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return draw_text(self, point, H_)

def draw_vertical(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return draw_text(self, point, V_)

def draw_perpendicular(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return draw_text(self, point, P_)

def draw_parallel(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return draw_text(self, point, PARA_)

def draw_line_info(self: 'SLINE', point: PointF) -> typing.List[QGraphicsTextItem] | bool:
    # locate the position of text
    font = QFont(ASSIST_FONT_FAMILY, ASSIST_FONT_SIZE)
    len_info = LENf.format(round(PointF.distance(point - self.selected_graphics_object.all()[0]), ASSISIT_PRECISION))
    arg_info = ARGf.format(round(PointF.arg(point - self.selected_graphics_object.all()[0]), ASSISIT_PRECISION))
    fm = QFontMetrics(font)
    width = fm.horizontalAdvance(len_info)
    height = fm.height()

    # point position
    # first kind of placement
    # left_point
    lp = self.gv_graphics.mapToScene(QPoint(0, 0))
    view_rect = self.gv_graphics.rect().toRectF()

    # point - lp
    # mapping

    rect = QRectF(point.x - lp.x(), point.y - 2 * height - lp.y(), width, 2 * height)
    if view_rect.contains(rect):
        p1 = PointF(point.x, point.y - 2 * height)
        p2 = PointF(point.x, point.y - height)
        
        return [draw_text(self, p1, len_info, font), draw_text(self, p2, arg_info, font)]
    # second kind of placement
    rect = QRectF(point.x - width - lp.x(), point.y - 2 * height - lp.y(), width, 2 * height)
    if view_rect.contains(rect):
        p1 = PointF(point.x - width, point.y - 2 * height)
        p2 = PointF(point.x - width, point.y - height)
        
        return [draw_text(self, p1, len_info, font), draw_text(self, p2, arg_info, font)]
    # third kind of placement
    rect = QRectF(point.x - width - lp.x(), point.y - lp.y(), width, 2 * height)
    if view_rect.contains(rect):
        p1 = PointF(point.x - width, point.y)
        p2 = PointF(point.x - width, point.y + height)
        
        return [draw_text(self, p1, len_info, font), draw_text(self, p2, arg_info, font)]
    # fourth kind of placement
    rect = QRectF(point.x - lp.x(), point.y + MOUSE_OCCLUSION_DISTANCE - lp.y(), width, 2 * height)
    if view_rect.contains(rect):
        p1 = PointF(point.x, point.y + MOUSE_OCCLUSION_DISTANCE)
        p2 = PointF(point.x, point.y + MOUSE_OCCLUSION_DISTANCE + height)
        
        return [draw_text(self, p1, len_info, font), draw_text(self, p2, arg_info, font)]
    return False

def draw_text(self: 'SLINE', point: PointF, text: str, font: QFont = None) -> QGraphicsTextItem:
    item = QGraphicsTextItem(text)
    item.setPos(QPointF(point.x, point.y))
    if font:
        item.setFont(font)
    self.gv_graphics.scene().addItem(item)
    return item
