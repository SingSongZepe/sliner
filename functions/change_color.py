import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from event.draw_point_event import DrawPointEvent
from event.draw_line_event import DrawLineEvent
from value.strings import *

def change_to_selected(self: 'SLINE'):    
    change_color(self, selected_color)

def change_to_default(self: 'SLINE'):
    change_color(self, default_color)

def change_color(self: 'SLINE', color: Qt.GlobalColor = selected_color):
    # change color or all selected_object
    for draw_event in self.selected_events.all():
        if isinstance(draw_event, DrawPointEvent) or isinstance(draw_event, DrawLineEvent):
            draw_event.item.change_color(color)

