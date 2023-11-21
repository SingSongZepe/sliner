import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.constrained import ConstrainCondition

def process_assist_point(self: 'SLINE', point: PointF) -> None:
    constrained_point = self.constrain_point(point)
    point = constrained_point.point
    
    if constrained_point.condition == ConstrainCondition.InLine:
        point_assist_item = self.draw_assist_point(point)
        self.assist_graphics_item.append(point_assist_item)