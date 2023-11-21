import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from value.strings import *

def unselect(self: 'SLINE') -> None:
    # change selected_objects color to default
    self.change_to_default()
    #
    self.selected_events.cls()