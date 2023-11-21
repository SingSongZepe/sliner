import typing

from PySide6.QtWidgets import QGraphicsItem

class SelectedItem:
    def __init__(self):
        self.selected_item: typing.List[QGraphicsItem] = []
    def append(self, item: QGraphicsItem) -> None:
        self.selected_item.append(item)
    def pop(self) -> QGraphicsItem | bool:
        return self.selected_item.pop() if self.selected_item else False
    def cls(self) -> None:
        self.selected_item = []

    def all(self) -> typing.List[QGraphicsItem]:
        return self.selected_item