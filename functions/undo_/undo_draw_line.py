import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_line_event import DrawLineEvent

def undo_draw_line(self: 'SLINE', draw_event: DrawLineEvent):
    self.graphics_lines.remove(draw_event.line)
    for p in draw_event.line.points:
        if self.graphics_points.exist(p):
            if p_ := self.graphics_points.get(p):
                self.graphics_points.remove(p_)
    self.gv_graphics.scene().removeItem(draw_event.item)
