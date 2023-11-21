import enum
import typing

from object.point import PointF
from object.line import LineF

class ConstrainCondition(enum.Enum):
    None_ = 0
    Horizontal = 1
    Vertical = 2
    Perpendicular = 3
    InLine = 4
    CurrentPoint = 5
    HorizontalInLine = 6
    VerticalInLine = 7
    Parallel = 8

class Constrained:
    pass

class ConstrainedPoint(Constrained):
    def __init__(self, point: PointF, condition: ConstrainCondition, constrained_by: typing.List[PointF | LineF] = None):
        self.point = point
        self.condition = condition  
        self.constrained_by = constrained_by
