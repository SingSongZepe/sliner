import typing

from event.draw_event import DrawEvent

class SelectedEvents:
    def __init__(self):
        self.selected_item: typing.List[DrawEvent] = []
    def append(self, item: DrawEvent) -> None:
        self.selected_item.append(item)
    def pop(self) -> DrawEvent | bool:
        return self.selected_item.pop() if self.selected_item else False
    def cls(self) -> None:
        self.selected_item = []
    def all(self) -> typing.List[DrawEvent]:
        return self.selected_item
    def exist(self, draw_event: DrawEvent) -> None:
        return draw_event in self.selected_item
    def remove(self, draw_event: DrawEvent) -> None:
        self.selected_item.remove(draw_event)

