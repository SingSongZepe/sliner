import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from event.delete_event_event import DeleteEventEvent
from event.trim_event import TrimEvent
from utils.common.log import *

def redo(self: 'SLINE'):
    if draw_event := self.redo_stack.pop():
        if isinstance(draw_event, DrawPointEvent):
            self.redo_draw_point(draw_event)
        elif isinstance(draw_event, DrawLineEvent):
            self.redo_draw_line(draw_event)
        # redo deleted events is undo
        elif isinstance(draw_event, DeleteEventEvent):
            self.redo_delete_event(draw_event)
        elif isinstance(draw_event, TrimEvent):
            self.redo_trim(draw_event)
        self.undo_stack.append(draw_event)

        ln('redo draw one or more graphics done')
    else:
        lw('no item in redo stack')