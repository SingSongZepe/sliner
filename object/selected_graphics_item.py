import typing

from PySide6.QtWidgets import QGraphicsItem

class SelectedGraphicsItem:
    def __init__(self):
        self.selected_graphics_item: typing.List[QGraphicsItem] = []
    def append(self, item: QGraphicsItem) -> None:
        self.selected_graphics_item.append(item)
    def pop(self) -> QGraphicsItem | bool:
        return self.selected_graphics_item.pop() if self.selected_graphics_item else False
    def cls(self) -> None:
        self.selected_graphics_item = []

    def all(self) -> typing.List[QGraphicsItem]:
        return self.selected_graphics_item