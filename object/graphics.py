import typing

from object.point import PointF
from object.line import LineF

class GraphicsObjects:
    pass

class GraphicsPoints(GraphicsObjects):
    def __init__(self) -> None:
        self.graphics_points: typing.List[PointF] = []
    def append(self, point: PointF) -> None:
        self.graphics_points.append(point)
    def pop(self) -> PointF:
        return self.graphics_points.pop()
    def remove(self, point: PointF) -> None:
        self.graphics_points.remove(point) if point in self.graphics_points else None
    def exist(self, point: PointF) -> bool:
        # using p == point
        # you needed to implement __eq__ function first
        return any(p for p in self.graphics_points if p == point)
    def get(self, point: PointF) -> PointF | bool:
        return next((p for p in self.graphics_points if p == point), False)
    
    # O(n)
    def near_a_point(self, pos: PointF) -> bool:
        return any(p.near(pos) for p in self.graphics_points)
    # O(n)
    def near_which_point(self, pos: PointF) -> PointF | bool:
        for p in self.graphics_points:
            if p.near(pos):
                return p
        return False

class GraphicsLines(GraphicsObjects):
    def __init__(self) -> None:
        self.graphics_lines: typing.List[LineF] = []
    def append(self, line: LineF) -> None:
        self.graphics_lines.append(line)
    def pop(self) -> LineF:
        return self.graphics_points.pop()
    def remove(self, line: LineF) -> None:
        self.graphics_lines.remove(line) if line in self.graphics_lines else None
    def exist(self, line: LineF) -> bool:
        # if you don't want to overlap lines
        # return any(l for l in self.graphics_lines if l == line)

        # allow you can overlap lines
        return False
    
    def near_a_line(self, pos: PointF) -> bool:
        return any(line.near(pos) for line in self.graphics_lines)
    def near_which_line(self, pos: PointF) -> LineF | bool:
        for l in self.graphics_lines:
            if l.near(pos):
                return l
        return False
    
    def near_a_segment(self, pos: PointF) -> bool:
        return any(line.near(pos) and line.on_segment(pos) for line in self.graphics_lines)
    def near_which_segment(self, pos: PointF) -> LineF | bool:
        for l in self.graphics_lines:
            if l.near(pos) and l.on_segment(pos):
                return l
        return False
    
    def perpendicular_a_line(self, line: LineF) -> bool:
        return any(l.perpendicular(line) for l in self.graphics_lines)
    def perpendicular_which_line(self, line: LineF) -> LineF | bool:
        for l in self.graphics_lines:
            # the p2 is second point while drawing a line, so use as near judgement
            if l.near(line.p2) and l.perpendicular(line):
                return l
        return False
    
    def parallel_a_line(self, line: LineF) -> bool:
        return any(l.parallel(line) for l in self.graphics_lines)
    def parallel_which_line(self, line: LineF) -> LineF | bool:
        for l in self.graphics_lines:
            if l.parallel(line):
                return l
        return False
    
    def intersect_point_list(self, line: LineF) -> typing.List[PointF]:
        intersect_points: typing.List[PointF] = []
        for l in self.graphics_lines:
            if l.intersect(line):
                intersect_points.append(l.get_intersect_point(line))
        return intersect_points

    
