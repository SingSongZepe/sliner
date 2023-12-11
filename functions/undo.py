import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from event.delete_event_event import DeleteEventEvent
from event.trim_event import TrimEvent
from utils.common.log import *

def undo(self: 'SLINE'):
    if draw_event := self.undo_stack.pop():
        if isinstance(draw_event, DrawPointEvent):
            self.undo_draw_point(draw_event)
        elif isinstance(draw_event, DrawLineEvent):
            self.undo_draw_line(draw_event)
        # undo event that deleted is do
        elif isinstance(draw_event, DeleteEventEvent):
            self.undo_delete_event(draw_event)
        # there if draw_line_event that trim_event contains, they may be already deleted by delete_event_event.
        # so there you just throw those event whose item is empty in GraphicsScene
        elif isinstance(draw_event, TrimEvent):
            self.undo_trim(draw_event)
        self.redo_stack.append(draw_event)

        ln('undo draw one or more graphics done')
    else:
        lw('no item in undo stack')

