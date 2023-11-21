import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.mode import Mode
from object.point import PointF
from object.line import LineF
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from value.strings import *

from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

# PointF LineF
def mouse_double_click(self: 'SLINE', eve: QMouseEvent):

    pos = eve.pos()
    spos = self.gv_graphics.mapToScene(pos)
    point = PointF(spos.x(), spos.y())

    if Mode.eq(self.mode, Mode.Emp):
        # the selected_point 
        if p := self.select_point(point):
            if draw_point_event := self.undo_stack.get_event(p):
                # change it color to selected_color
                draw_point_event.item.change_color(selected_color)
                self.selected_events.append(draw_point_event)
                return
        elif l := self.select_line(point):
            if draw_line_event := self.undo_stack.get_event(l):
                draw_line_event.item.change_color(selected_color)
                self.selected_events.append(draw_line_event)
                return







