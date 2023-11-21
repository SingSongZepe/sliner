import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from event.delete_event_event import DeleteEventEvent
from utils.common.log import *

def redo(self: 'SLINE'):
    if draw_event := self.redo_stack.pop():
        if isinstance(draw_event, DrawPointEvent):
            self.graphics_points.append(draw_event.point)
            self.gv_graphics.scene().addItem(draw_event.item)
        elif isinstance(draw_event, DrawLineEvent):
            self.graphics_lines.append(draw_event.line)
            self.gv_graphics.scene().addItem(draw_event.item)
        # redo deleted events is undo
        elif isinstance(draw_event, DeleteEventEvent):
            for dw in draw_event.draw_events:
                if isinstance(dw, DrawPointEvent):
                    self.graphics_points.remove(dw.point)
                    self.gv_graphics.scene().removeItem(dw.item)
                elif isinstance(dw, DrawLineEvent):
                    self.graphics_lines.remove(dw.line)
                    self.gv_graphics.scene().removeItem(dw.item) 
        self.undo_stack.append(draw_event)

        ln('redo draw one or more graphics done')
    else:
        lw('no item in redo stack')