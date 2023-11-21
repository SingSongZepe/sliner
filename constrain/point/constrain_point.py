import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.constrained import ConstrainCondition, ConstrainedPoint

def constrain_point(self: 'SLINE', point: PointF) -> ConstrainedPoint:
    # select current point
    # Priority 0 (current point)
    if self.graphics_points.near_a_point(point):
        return ConstrainedPoint(self.graphics_points.near_which_point(point), ConstrainCondition.CurrentPoint)

    # Priority 1 (in line)
    if line := self.graphics_lines.near_which_line(point):
        return ConstrainedPoint(line.get_perpendicular_point(point), ConstrainCondition.InLine, [line])
    
    # Priority 2 


    # Priority n (all point)
    return ConstrainedPoint(point, ConstrainCondition.None_)

