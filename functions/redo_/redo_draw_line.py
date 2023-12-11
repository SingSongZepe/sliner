import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_line_event import DrawLineEvent
from utils.common.log import *

def redo_draw_line(self: 'SLINE', draw_event: DrawLineEvent):
    self.graphics_lines.append(draw_event.line)
    for p in draw_event.line.points:
        if not self.graphics_points.exist(p):
            self.graphics_points.append(p)
    self.gv_graphics.scene().addItem(draw_event.item)
