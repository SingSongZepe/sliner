from typing import overload

from err.parameter import ParameterNotCorrectError
from err.graphics import UnknownGraphicsObjectError
from object.point import PointF
from object.line import LineF

class RectF:
    @overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        ...
    @overload
    def __init__(self, p1: PointF, p2: PointF):
        ...
    def __init__(self, *args):
        if len(args) == 4:
            self.p1 = PointF(args[0], args[1])
            self.p2 = PointF(args[2], args[3])
        elif len(args) == 2:
            self.p1 = args[0]
            self.p2 = args[1]
        else:
            raise ParameterNotCorrectError('error number of arguments not correct')
    
    def point_in_rect(self, point: PointF) -> bool:
        return (point.x < max(self.p1.x, self.p2.x) and point.y < max(self.p1.y, self.p2.y)) and (point.x > min(self.p1.x, self.p2.x) and point.y > min(self.p1.y, self.p2.y))
    
    def poly_in_rect(self, obj: PointF | LineF) -> bool:
        if isinstance(obj, PointF):
            return self.point_in_rect(obj)
        elif isinstance(obj, LineF):
            return self.point_in_rect(obj.p1) and self.point_in_rect(obj.p2)
        raise UnknownGraphicsObjectError('unknown graphics objects')
