import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.mode import Mode
from utils.common.log import *

def toggle_mode(self: 'SLINE', mode: Mode):
    self.mode = mode
    # there must clear cache
    # for example, if user select a point and then toggle mode
    # the select_points must be empty list

    # clear assist
    self.clear_assist()

    # selected graphics for helping constructing graphics item 
    self.selected_graphics_object.cls()
    for item in self.selected_graphics_item.all():
        self.gv_graphics.scene().removeItem(item)
    self.selected_graphics_item.cls()

    ln('toggle to mode ' + Mode.string(mode))
