import typing

from event.draw_event import DrawEvent

# this event when select some point and delete them
# this event is also draw_event
class DeleteEventEvent(DrawEvent):
    def __init__(self, draw_events: typing.List[DrawEvent]):
        self.draw_events = draw_events
