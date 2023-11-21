import typing

from event.draw_event import DrawEvent
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from object.point import PointF
from object.line import LineF

class UndoStack:
    def __init__(self) -> None:
        self.undo_stack: typing.List[DrawEvent] = []
    def append(self, draw_event: DrawEvent) -> None:
        self.undo_stack.append(draw_event)
    def pop(self) -> DrawEvent | bool:
        return self.undo_stack.pop() if self.undo_stack else False
    def all(self) -> typing.List[DrawEvent]:
        return self.undo_stack
    def cls(self) -> None:
        self.undo_stack = []
    def remove(self, draw_event: DrawEvent) -> bool:
        if draw_event in self.undo_stack:
            self.undo_stack.remove(draw_event)
            return True
        return False
    
    def get_event(self, graphics_object: PointF | LineF) -> DrawEvent:
        # get draw_point_event
        if isinstance(graphics_object, PointF):
            for draw_event in self.undo_stack:
                if isinstance(draw_event, DrawPointEvent):
                    if draw_event.point == graphics_object:
                        return draw_event
        # get draw_line_event
        elif isinstance(graphics_object, LineF):
            for draw_event in self.undo_stack:
                if isinstance(draw_event, DrawLineEvent):
                    if draw_event.line == graphics_object:
                        return draw_event

class RedoStack:
    def __init__(self) -> None:
        self.redo_stack: typing.List[DrawEvent] = []
    def append(self, draw_event: DrawEvent) -> None:
        self.redo_stack.append(draw_event)
    def pop(self) -> DrawEvent | bool:
        return self.redo_stack.pop() if self.redo_stack else False
    # use to cls
    def all(self) -> typing.List[DrawEvent]:
        return self.redo_stack
    def cls(self) -> None:
        self.redo_stack = []