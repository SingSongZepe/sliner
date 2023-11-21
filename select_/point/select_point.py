import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF

def select_point(self: 'SLINE', point: PointF) -> PointF:
    return self.graphics_points.near_which_point(point)
