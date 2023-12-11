import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.trim_event import TrimEvent
from utils.common.log import *

def redo_trim(self: 'SLINE', draw_event: TrimEvent):
    self.redo_delete_event(draw_event.delete_event_event)
    for dw in draw_event.draw_events:
        self.redo_draw_line(dw)
