import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.rect import RectF
from object.mode import Mode
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
    self.indicate_mouse_pos(point)

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
        self.process_assist_point(point)
    
    # Line Mode
    elif Mode.eq(self.mode, Mode.Line):
        self.process_assist_line(point)



