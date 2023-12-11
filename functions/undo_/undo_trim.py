import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.trim_event import TrimEvent

def undo_trim(self: 'SLINE', draw_event: TrimEvent):
    self.undo_delete_event(draw_event.delete_event_event)
    for dw in draw_event.draw_events:
        if dw.item in self.gv_graphics.scene().items():
            self.undo_draw_line(dw)

