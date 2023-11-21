import typing

from event.delete_event_event import DeleteEventEvent
from event.draw_line_event import DrawLineEvent
from event.draw_event import DrawEvent

class TrimEvent(DrawEvent):
    def __init__(self, delete_event_event: DeleteEventEvent, draw_events: typing.List[DrawLineEvent]) -> None:
        self.delete_event_event = delete_event_event
        # maybe also DrawArcEvent, but there don't concern about arc
        self.draw_events = draw_events
