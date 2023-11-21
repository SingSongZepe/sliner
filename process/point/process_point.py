import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from event.draw_point_event import DrawPointEvent

def process_point(self: 'SLINE', point: PointF) -> None:
    constrained_point = self.constrain_point(point)
    point = constrained_point.point
    
    if self.graphics_points.exist(point): # point exist
        point = self.graphics_points.get(point)
    else: # not exist, so draw it
        self.graphics_points.append(point)
        point_item = self.draw_point(point)
        self.undo_stack.append(DrawPointEvent(point, point_item))