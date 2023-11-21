import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.rect import RectF
from object.mode import Mode
from object.constrained import ConstrainCondition
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from value.value import *
from value.strings import *

from PySide6.QtGui import QMouseEvent, QCursor
from PySide6.QtCore import Qt

def mouse_move(self: 'SLINE', eve: QMouseEvent) -> None:
    # delete all assist graphics
    self.clear_assist()

    pos = eve.pos()
    spos = self.gv_graphics.mapToScene(pos)
    point = PointF(spos.x(), spos.y())

    if Mode.eq(self.mode, Mode.Emp):
        if self._rect_select:
            rect = RectF(self._rect_select_start_pos, point)
            # draw assist_rect
            rect_item = self.draw_assist_rect(rect)
            self.assist_graphics_item.append(rect_item)

            # selected event
            for draw_event in self.undo_stack.all():
                if isinstance(draw_event, DrawPointEvent):
                    # in rect
                    if rect.poly_in_rect(draw_event.point):
                        if not self.selected_events.exist(draw_event):
                            draw_event.item.change_color(selected_color)
                            self.selected_events.append(draw_event)
                    else:
                        if self.selected_events.exist(draw_event):
                            draw_event.item.change_color(default_color)
                            self.selected_events.remove(draw_event)
                elif isinstance(draw_event, DrawLineEvent):
                    if rect.poly_in_rect(draw_event.line):
                        if not self.selected_events.exist(draw_event):
                            draw_event.item.change_color(selected_color)
                            self.selected_events.append(draw_event)
                    else:
                        if self.selected_events.exist(draw_event):
                            draw_event.item.change_color(default_color)
                            self.selected_events.remove(draw_event)
        elif self._tran:
            delta = self.gv_graphics.mapToScene(self._tran_start_pos.to_QPoint()) - self.gv_graphics.mapToScene(pos)
            self.gv_graphics.horizontalScrollBar().setValue(self.gv_graphics.horizontalScrollBar().value() + delta.x() / VIEW_TRANSLATE_FACTORS)
            self.gv_graphics.verticalScrollBar().setValue(self.gv_graphics.verticalScrollBar().value() + delta.y() / VIEW_TRANSLATE_FACTORS)
            # self._tran_start_pos = point
            return
    
    # Current Point Reminder
    if self.graphics_points.near_a_point(point):
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    else:
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

    # Point Mode
    if Mode.eq(self.mode, Mode.Point):
        constrained_point = self.constrain_point(point)
        point = constrained_point.point
        
        if constrained_point.condition == ConstrainCondition.InLine:
            point_assist_item = self.draw_assist_point(point)
            self.assist_graphics_item.append(point_assist_item)
    
    # Line Mode
    elif Mode.eq(self.mode, Mode.Line):
        constrained_point = self.constrain_line(point)
        point = constrained_point.point

        # process constrain
        if constrained_point.condition == ConstrainCondition.Horizontal or constrained_point.condition == ConstrainCondition.HorizontalInLine:
            # there must exist a point in sgo and it is the a PointF object
            text_assist_item = self.draw_assist_horizontal((self.selected_graphics_object.all()[0] + point) / 2)
            self.assist_graphics_item.append(text_assist_item)
        elif constrained_point.condition == ConstrainCondition.Vertical or constrained_point.condition == ConstrainCondition.VerticalInLine:
            text_assist_item = self.draw_assist_vertical((self.selected_graphics_object.all()[0] + point) / 2)
            self.assist_graphics_item.append(text_assist_item)
        elif constrained_point.condition == ConstrainCondition.InLine:
            point_assist_item = self.draw_assist_point(point)
            self.assist_graphics_item.append(point_assist_item)
        elif constrained_point.condition == ConstrainCondition.Perpendicular:
            text_assist_item = self.draw_assist_perpendicular((self.selected_graphics_object.all()[0] + point) / 2)
            self.assist_graphics_item.append(text_assist_item)
        elif constrained_point.condition == ConstrainCondition.Parallel:
            text_assist_item = self.draw_assist_parallel((self.selected_graphics_object.all()[0] + point) / 2)
            self.assist_graphics_item.append(text_assist_item)

        # meet the condition of constructing a assist line
        if self.selected_graphics_object.for_assist_line():
            line_assist_item = self.draw_assist_line(self.selected_graphics_object.all()[0], point)
            self.assist_graphics_item.append(line_assist_item)
        
        if self.selected_graphics_object.for_assist_line_info():
            if (text_assist_item := self.draw_assist_line_info(point)) and text_assist_item[0]:
                for item in text_assist_item:
                    self.assist_graphics_item.append(item)




