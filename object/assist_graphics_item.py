import typing

from object.selected_graphics_objects import SelectedGraphicsObjects
from object.point import PointF

from PySide6.QtWidgets import QGraphicsItem

class AssistGraphicsItem:
    def __init__(self) -> None:
        self.assist_graphics_item: typing.List[QGraphicsItem] = []
    def append(self, item: QGraphicsItem):
        self.assist_graphics_item.append(item)
    def pop(self) -> QGraphicsItem | bool:
        return self.assist_graphics_item.pop() if self.assist_graphics_item else False
    def all(self) -> typing.List[QGraphicsItem]:
        return self.assist_graphics_item
    def cls(self) -> None:
        self.assist_graphics_item = []
        
    # for constructing a assist line
    # may be it is the function of SelectGraphicsObjects
    def for_line(self, sgo: SelectedGraphicsObjects) -> bool:
        return len(sgo.all()) == 1 and isinstance(sgo.all()[0], PointF)
    