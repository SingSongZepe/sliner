import typing

from object.point import PointF
from object.line import LineF


# this class is not selected_graphics_objects
# when user in mode Emp, then can select graphics objects
# and in the same time, its color will be turned to darkyellow
class SelectedObjects:
    def __init__(self):
        self.selected_objects = []
    def append(self, obj: PointF | LineF) -> None:
        self.selected_objects.append(obj)
    def pop(self) -> (PointF | LineF) | bool:
        return self.selected_objects.pop() if self.selected_objects else False
    def cls(self) -> None:
        self.selected_objects = []
    def all(self) -> typing.List[PointF | LineF]:
        return self.selected_objects

