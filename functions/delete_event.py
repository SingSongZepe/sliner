import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from event.delete_event_event import DeleteEventEvent

def delete_event(self: 'SLINE') -> DeleteEventEvent:
    for draw_event in self.selected_events.all():
        if isinstance(draw_event, DrawPointEvent):
            self.graphics_points.remove(draw_event.point)
            self.gv_graphics.scene().removeItem(draw_event.item)
            self.undo_stack.remove(draw_event)
        elif isinstance(draw_event, DrawLineEvent):
            self.graphics_lines.remove(draw_event.line)
            self.gv_graphics.scene().removeItem(draw_event.item)
            self.undo_stack.remove(draw_event)
    delete_event_event = DeleteEventEvent(self.selected_events.all())
    self.selected_events.cls()
    return delete_event_event
