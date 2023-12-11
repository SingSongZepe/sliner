import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent

def undo_draw_point(self: 'SLINE', draw_event: DrawPointEvent):
    self.graphics_points.remove(draw_event.point) 
    self.gv_graphics.scene().removeItem(draw_event.item)

