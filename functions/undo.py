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
            self.graphics_points.remove(draw_event.point) 
            self.gv_graphics.scene().removeItem(draw_event.item)
        elif isinstance(draw_event, DrawLineEvent):
            self.graphics_lines.remove(draw_event.line)
            self.gv_graphics.scene().removeItem(draw_event.item)
        # undo event that deleted is do
        elif isinstance(draw_event, DeleteEventEvent):
            for dw in draw_event.draw_events:
                self.undo_stack.append(dw)
                if isinstance(dw, DrawPointEvent):
                    self.graphics_points.append(dw.point)
                    self.gv_graphics.scene().addItem(dw.item)
                elif isinstance(dw, DrawLineEvent):
                    self.graphics_lines.append(dw.line)
                    self.gv_graphics.scene().addItem(dw.item)
        # there if draw_line_event that trim_event contains, they may be already deleted by delete_event_event.
        # so there you just throw those event whose item is empty in GraphicsScene
        elif isinstance(draw_event, TrimEvent):
            ln('trim event!')
        self.redo_stack.append(draw_event)

        ln('undo draw one or more graphics done')
    else:
        lw('no item in undo stack')

