import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.mode import Mode
from object.point import PointF
from object.line import LineF
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent

from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

def mouse_click(self: 'SLINE', eve: QMouseEvent) -> None:
    pos = eve.pos()
    spos = self.gv_graphics.mapToScene(pos)
    point = PointF(spos.x(), spos.y())
    
    # translating
    if Mode.eq(self.mode, Mode.Emp):
        # rect select
        if eve.button() == Qt.MouseButton.LeftButton and not eve.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self._rect_select = True
            self._rect_select_start_pos = point
            # return means it is unnecessary to clear redo_stack
            return
        # translate
        elif eve.button() == Qt.MouseButton.LeftButton and eve.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self._tran = True
            self._tran_start_pos = point
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            # return means it is unnecessary to clear redo_stack
            return

    if Mode.eq(self.mode, Mode.Point):
        constrained_point = self.constrain_point(point)
        point = constrained_point.point
        
        if self.graphics_points.exist(point): # point exist
            point = self.graphics_points.get(point)
        else: # not exist, so draw it
            self.graphics_points.append(point)
            point_item = self.draw_point(point)
            self.undo_stack.append(DrawPointEvent(point, point_item))
        # draw
    elif Mode.eq(self.mode, Mode.Line):
        # select point, appending to graphics_points
        constrained_point = self.constrain_line(point)
        point = constrained_point.point
        
        if self.graphics_points.exist(point):
            point = self.graphics_points.get(point)
            self.selected_graphics_object.append(point)
        else:
            self.graphics_points.append(point)
            point_item = self.draw_point(point)
            # for drawing a line, it assist draw point event is not a event that needed to append
            # self.undo_stack.append(DrawPointEvent(point, point_item))
            self.selected_graphics_object.append(point)
            self.selected_graphics_item.append(point_item)

        # meet the condition to draw a line
        if self.selected_graphics_object.for_line():
            if points := self.selected_graphics_object.get_objects(2):
                line = LineF(points[0], points[1])
                line_item = self.draw_line(points[0], points[1])
                self.undo_stack.append(DrawLineEvent(line, line_item))
                self.graphics_lines.append(line)

                # clear the select_graphics_object
                self.selected_graphics_object.cls()
                for item in self.selected_graphics_item.all():
                    self.gv_graphics.scene().removeItem(item)
                self.selected_graphics_item.cls()

    self.redo_stack.cls()



