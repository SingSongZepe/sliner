import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from event.delete_event_event import DeleteEventEvent

def undo_delete_event(self: 'SLINE', draw_event: DeleteEventEvent):
    for dw in draw_event.draw_events:
        self.undo_stack.append(dw)
        if isinstance(dw, DrawPointEvent):
            self.graphics_points.append(dw.point)
            self.gv_graphics.scene().addItem(dw.item)
        elif isinstance(dw, DrawLineEvent):
            self.graphics_lines.append(dw.line)
            self.gv_graphics.scene().addItem(dw.item)
            