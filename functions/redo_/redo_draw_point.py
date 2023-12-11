import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent
from utils.common.log import *

def redo_draw_point(self: 'SLINE', draw_event: DrawPointEvent):
    self.graphics_points.append(draw_event.point)
    self.gv_graphics.scene().addItem(draw_event.item)
    