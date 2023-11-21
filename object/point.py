from typing import overload
import math

from err.parameter import ParameterNotCorrectError
from object.color import Color
from value.strings import default_color
from value.value import near_length, angle_threshold

from PySide6.QtCore import QPointF, QPoint

class PointF:
    @overload
    def __init__(self, x: float, y: float) -> None:
        ...
    @overload
    def __init__(self, x: float, y: float, color: str | Color) -> None:
        ...
    def __init__(self, *args) -> None:
        self.x: float = args[0]
        self.y: float = args[1]
        if len(args) == 2: # no color provided
            self.color: Color = default_color
        elif isinstance(args[2], str):
            self.color: Color = Color(args[2])
        elif isinstance(args[2], Color):
            self.color: Color = args[2]
        else:
            raise ParameterNotCorrectError('error number of arguments not correct')

    def __add__(self, other: 'PointF') -> 'PointF':
        return PointF(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'PointF') -> 'PointF':
        return PointF(self.x - other.x, self.y - other.y)
    
    def __truediv__(self, scalar) -> 'PointF':
        return PointF(self.x / scalar, self.y / scalar)
    
    def __eq__(self, point: 'PointF') -> bool:
        return self.x == point.x and self.y == point.y

    def near(self, pos: 'PointF') -> bool:
        if abs(pos.x - self.x) < near_length and abs(pos.y - self.y) < near_length:
            return True
        return False

    def horizontal(self, pos: 'PointF') -> bool:
        angle = math.degrees(math.atan2(pos.y - self.y, pos.x - self.x))
        angle = (angle + 360) % 360 
        return abs(angle - 180) < angle_threshold or abs(angle - 0) < angle_threshold or abs(angle - 360) < angle_threshold

    def vertical(self, pos: 'PointF') -> bool:
        angle = math.degrees(math.atan2(pos.y - self.y, pos.x - self.x))
        angle = (angle + 360) % 360  
        return abs(angle - 90) < angle_threshold or abs(angle - 270) < angle_threshold

    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def arg(self):
        degrees = math.degrees(-math.atan2(self.y, self.x))
        return degrees if degrees >= 0 else degrees + 360

    def copy(self: 'PointF') -> 'PointF':
        return PointF(
            self.x,
            self.y
        )
    
    def to_QPointF(self) -> QPointF:
        return QPointF(self.x, self.y)

    def to_QPoint(self) -> QPoint:
        return QPoint(self.x, self.y)
    