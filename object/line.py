from typing import overload
import math
import numpy as np

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
                return
            raise TypeError('Line receive two points as its position')
        elif len(args) == 4:
            self.p1 = PointF(args[0], args[1])
            self.p2 = PointF(args[2], args[3])
    
    def __eq__(self, line: 'LineF') -> bool:
        return self.p1 == line.p1 and self.p2 == line.p2
    
    def near(self: 'LineF', point: PointF) -> bool:
        return abs((self.p2.y - self.p1.y) * point.x - (self.p2.x - self.p1.x) * point.y + self.p2.x * self.p1.y - self.p2.y * self.p1.x) / math.sqrt((self.p2.y - self.p1.y) ** 2 + (self.p2.x - self.p1.x) ** 2) <= near_length if (self.p2.y - self.p1.y) ** 2 + (self.p2.x - self.p1.x) ** 2 != 0 else False

    def ang(self) -> float:
        angle_deg = math.degrees(math.atan2(self.p2.y - self.p1.y, self.p2.x - self.p1.x))
        return angle_deg if angle_deg >= 0 else angle_deg + 360

    def k(self) -> float:
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x) if self.p2.x - self.p1.x != 0 else '' # '' not equals to False
    
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
            x2 = self.p2.x
            y2 = self.p2.y

            k = (y2 - y1) / (x2 - x1) # when slope is zero
            x = (x0 - x1) / (k * k + 1) + k * (y0 - y1) / (k * k + 1) + x1
            y = k * (x0 - x1) / (k * k + 1) + (k * k * y0 + y1) / (k * k + 1)
        return PointF(x, y)
    
    # get the parallel point
    def get_parallel_point(self: 'LineF', p: PointF, point: PointF) -> PointF:
        # p1 is the first point that users selected
        # point the mouse pos
        if self.k() == '':
            return PointF(p.x, point.y)
        elif self.k() == 0.0:
            return PointF(point.x, p.y)
        else:
            return LineF(p, PointF(point.x, self.k() * (point.x - p.x) + p.y)).get_perpendicular_point(point)
            # or
            # return LineF(p, PointF((point.y - p.y) / self.k() + p.x, point.y)).get_perpendicular_point(point)


    # ? no deviation judgement
    def horizontal(self: 'LineF') -> PointF:
        return self.k() == ''

    def get_horizontal_point(self: 'LineF', point: PointF) -> PointF | bool:
        if self.k() == '':
            return PointF(self.p1.x, point.y)
        elif self.k() == 0.0:
            return False  # horizontal point not exists
        else:
            return PointF((point.y - self.p1.y) / self.k() + self.p1.x, point.y)
        
    # ? no deviation judgement
    def vertical(self: 'LineF') -> PointF:
        return self.k() == 0.0
    
    def get_vertical_point(self: 'LineF', point: PointF) -> PointF | bool:
        if self.k() == '':
            return False
        elif self.k() == 0.0:
            return PointF(point.x, self.p1.y)
        else:
            return PointF(point.x, self.k() * (point.x - self.p1.x) + self.p1.y)
        