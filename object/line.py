from typing import overload
import math
import numpy as np

from err.parameter import ParameterNotCorrectError
from object.point import PointF
from value.value import *

class LineF:
    @overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        ...
    @overload
    def __init__(self, p1: PointF, p2: PointF):
        ...
    def __init__(self, *args):
        if len(args) == 2:
            if isinstance(args[0], PointF) and isinstance(args[1], PointF):
                self.p1 = args[0]
                self.p2 = args[1]
                self.cal_points()
                return
            raise TypeError('Line receive two points as its position')
        elif len(args) == 4:
            self.p1 = PointF(args[0], args[1])
            self.p2 = PointF(args[2], args[3])
            self.cal_points()
        else:
            raise ParameterNotCorrectError('error number of arguments not correct')
    
    def cal_points(self) -> None:
        self.points = [self.p1, self.p2]
    
    def __eq__(self, line: 'LineF') -> bool:
        return self.p1 == line.p1 and self.p2 == line.p2

    def __ne__(self, line: 'LineF') -> bool:
        return not self.__eq__(line)
    
    def near(self: 'LineF', point: PointF) -> bool:
        return abs((self.p2.y - self.p1.y) * point.x - (self.p2.x - self.p1.x) * point.y + self.p2.x * self.p1.y - self.p2.y * self.p1.x) / math.sqrt((self.p2.y - self.p1.y) ** 2 + (self.p2.x - self.p1.x) ** 2) <= near_length if (self.p2.y - self.p1.y) ** 2 + (self.p2.x - self.p1.x) ** 2 != 0 else False

    def ang(self) -> float:
        angle_deg = math.degrees(math.atan2(self.p2.y - self.p1.y, self.p2.x - self.p1.x))
        return angle_deg if angle_deg >= 0 else angle_deg + 360

    def k(self) -> float | None:
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x) if self.p2.x - self.p1.x != 0 else None # None not equals to False
    
    def yx(self, x: float) -> float:
        return self.k() * (x - self.p1.x) + self.p1.y if self.k() is not None else None
    
    def rect(self) -> 'RectF':
        from object.rect import RectF
        return RectF(self.p1, self.p2)

    def on_segment(self, point: PointF) -> bool:
        if self.k() is None:
            return point.y > min(self.p1.y, self.p2.y) and point.y < max(self.p1.y, self.p2.y)
        return point.x > min(self.p1.x, self.p2.x) and point.x < max(self.p1.x, self.p2.x)
    
    # this method is not that good to check whether perpendicular between two lines
    # def perpendicular(self: 'LineF', line: 'LineF') -> bool:
    #     if (self.p1.x == self.p2.x and line.p1.y == line.p2.y) or (self.p1.y == self.p2.y and line.p1.x == line.p2.x):
    #         return True
    #     kk = -self.k() * line.k()
    #     if kk < PERPENDICULAR_UPPER_BOUND and kk > PERPENDICULAR_LOWER_BOUND:
    #         return True
    #     return False

    # ? there be some deviation when judge as perpendicular
    def perpendicular(self: 'LineF', line2: 'LineF') -> bool:
        direction_vector1 = (self.p2.x - self.p1.x, self.p2.y - self.p1.y)
        direction_vector2 = (line2.p2.x - line2.p1.x, line2.p2.y - line2.p1.y)

        dot_product = direction_vector1[0] * direction_vector2[0] + direction_vector1[1] * direction_vector2[1]
        norm_product = math.sqrt(direction_vector1[0]**2 + direction_vector1[1]**2) * math.sqrt(direction_vector2[0]**2 + direction_vector2[1]**2)
        angle = math.acos(dot_product / norm_product)

        if math.degrees(np.abs(angle - np.pi /2)) < angle_threshold:
            return True
        else:
            return False
    
    # ? there be deviation judgement
    def parallel(self: 'LineF', line: PointF) -> bool:
        v1 = np.array([self.p2.x - self.p1.x, self.p2.y - self.p1.y])
        v2 = np.array([line.p2.x - line.p1.x, line.p2.y - line.p1.y])

        angle = math.degrees(np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))

        if abs(angle) < angle_threshold:
            return True
        else:
            return False
    
    # get the perpendicular point
    def get_perpendicular_point(self: 'LineF', point: PointF) -> PointF:
        if self.p1.x == self.p2.x:  # when slope is infinite
            x = self.p1.x
            y = point.y
        elif self.p1.y == self.p2.y:
            x = point.x
            y = self.p1.y
        else:
            x0 = point.x
            y0 = point.y
            x1 = self.p1.x
            y1 = self.p1.y

            k = self.k() # when slope is zero
            x = (x0 - x1) / (k * k + 1) + k * (y0 - y1) / (k * k + 1) + x1
            y = k * (x0 - x1) / (k * k + 1) + (k * k * y0 + y1) / (k * k + 1)
        return PointF(x, y)
    
    # get the parallel point
    def get_parallel_point(self: 'LineF', p: PointF, point: PointF) -> PointF:
        # p1 is the first point that users selected
        # point the mouse pos
        if self.k() is None:
            return PointF(p.x, point.y)
        elif self.k() == 0.0:
            return PointF(point.x, p.y)
        else:
            return LineF(p, PointF(point.x, self.k() * (point.x - p.x) + p.y)).get_perpendicular_point(point)
            # or
            # return LineF(p, PointF((point.y - p.y) / self.k() + p.x, point.y)).get_perpendicular_point(point)

    def get_parallel_isolength_point(self: 'LineF', p_: PointF, p: PointF) -> PointF:
        # p_ self point
        # p another point

        # ??? what this skills?
        line = LineF(p, p_)
        line.k = lambda : self.k()
        return line.get_perpendicular_point(p_)

    # 
    def intersect(self: 'LineF', line: 'LineF') -> bool:
        if not self.rect().intersect(line.rect()):
            return False
        return True if self.get_intersect_point(line) else False

    def get_intersect_point(self: 'LineF', line: 'LineF') -> PointF | bool:
        if self.k() == line.k():
            return False
        elif self.k() is None:
            return PointF(self.p1.x, line.yx(self.p1.x)) if line.on_segment(PointF(self.p1.x, line.yx(self.p1.x))) else False
        elif line.k() is None:
            return PointF(line.p1.x, self.yx(line.p1.x)) if self.on_segment(PointF(line.p1.x, self.yx(line.p1.x))) else False
        x = (line.k() * line.p1.x - line.p1.y - self.k() * self.p1.x + self.p1.y) / (line.k() - self.k())
        y = (self.k() * line.k() * (line.p1.x - self.p1.x) + line.k() * self.p1.y - self.k() * line.p1.y) / (line.k() - self.k())
        return PointF(x, y) if self.on_segment(PointF(x, y)) else False

    # ? no deviation judgement
    def horizontal(self: 'LineF') -> bool:
        return self.k() == 0.0 

    def get_horizontal_point(self: 'LineF', point: PointF) -> PointF | bool:
        if self.k() is None:
            return PointF(self.p1.x, point.y)
        elif self.k() == 0.0:
            return False  # horizontal point not exists
        else:
            return PointF((point.y - self.p1.y) / self.k() + self.p1.x, point.y)
        
    # ? no deviation judgement
    def vertical(self: 'LineF') -> bool:
        return self.k() is None
    
    def get_vertical_point(self: 'LineF', point: PointF) -> PointF | bool:
        if self.k() is None:
            return False
        elif self.k() == 0.0:
            return PointF(point.x, self.p1.y)
        else:
            return PointF(point.x, self.k() * (point.x - self.p1.x) + self.p1.y)
    
    # angle when no other constrained
    # the first point of the line is "based point"
    # the second point of the line is "to set point"
    def get_integer_ang_point(self) -> PointF:
        if self.k() is None or self.k() == 0.0:
            return self.p2
        ang = self.ang() // 1 # integer angle
        print(ang)
        if ang % 90 == 0.0:
            return self.p2

        k = math.tan(ang * math.pi / 180)
        y1 = k * (self.p2.x - self.p1.x) + self.p1.y
        x2 = (self.p2.y - self.p1.y) / k + self.p1.x

        if math.fabs(y1 - self.p2.y) < math.fabs(x2 - self.p2.x):
            return PointF(self.p2.x, y1)
        else:
            return PointF(x2, self.p2.y)
        