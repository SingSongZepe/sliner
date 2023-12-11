import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.delete_event_event import DeleteEventEvent
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from utils.common.log import *

def redo_delete_event(self: 'SLINE', draw_event: DeleteEventEvent):
    for dw in draw_event.draw_events:
        if isinstance(dw, DrawPointEvent):
            self.undo_draw_point(dw)
        elif isinstance(dw, DrawLineEvent):
            self.undo_draw_line(dw)
