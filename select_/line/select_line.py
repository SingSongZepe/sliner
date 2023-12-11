import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.line import LineF

def select_line(self: 'SLINE', point: PointF) -> LineF:
    return self.graphics_lines.near_which_segment(point)
