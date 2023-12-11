import typing

from object.point import PointF
from object.line import LineF

class SelectedGraphicsObjects:
    def __init__(self) -> None:
        self.selected_graphics_objects: typing.List[PointF | LineF] = []
    def append(self, obj: PointF | LineF) -> None:
        self.selected_graphics_objects.append(obj)
    def pop(self) -> (PointF | LineF) | bool:
        return self.selected_graphics_objects.pop() if self.selected_graphics_objects else False
    def cls(self) -> None:
        self.selected_graphics_objects = []
    def all(self) -> typing.List[PointF | LineF]:
        return self.selected_graphics_objects

    # two point already in stack
    # enough for drawing a line
    # ! real
    def for_line(self) -> bool:
        return True if len(self.selected_graphics_objects) == 2 and isinstance(self.selected_graphics_objects[0], PointF) and isinstance(self.selected_graphics_objects[1], PointF) else False
    
    # ! assist
    def for_assist_line(self) -> bool:
        return True if len(self.selected_graphics_objects) == 1 and isinstance(self.selected_graphics_objects[0], PointF) else False
    def for_assist_line_info(self) -> bool:
        return self.for_assist_line()

    def get_objects(self, num: int) -> typing.List[PointF | LineF]:
        return [self.selected_graphics_objects[i] for i in range(num)] if isinstance(num, int) else []
        