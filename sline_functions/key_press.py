import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from utils.common.log import *
from object.mode import Mode
from event.delete_event_event import DeleteEventEvent

from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

def key_press(self: 'SLINE', eve: QKeyEvent) -> None:
    # undo
    if eve.key() == Qt.Key.Key_Z and eve.modifiers() & Qt.KeyboardModifier.ControlModifier:
        self.undo()
        return
    # redo
    elif eve.key() == Qt.Key.Key_Y and eve.modifiers() & Qt.KeyboardModifier.ControlModifier:
        self.redo()
        return
    # unselect
    elif eve.key() == Qt.Key.Key_Escape:
        self.unselect()
        return
    # delete
    elif eve.key() == Qt.Key.Key_Delete:
        self.change_to_default()
        delete_event_event: DeleteEventEvent = self.delete_event()
        self.undo_stack.append(delete_event_event)
        return
    elif eve.key() == Qt.Key.Key_E:
        self.toggle_mode(Mode.Emp)
        return
    elif eve.key() == Qt.Key.Key_P:
        self.toggle_mode(Mode.Point)
        return
    elif eve.key() == Qt.Key.Key_L:
        self.toggle_mode(Mode.Line)
        return
    elif eve.key() == Qt.Key.Key_A:
        self.toggle_mode(Mode.Arc)
        return
    elif eve.key() == Qt.Key.Key_T:
        self.toggle_mode(Mode.Trim)
    elif eve.key() == Qt.Key.Key_D:
        self.toggle_mode(Mode.Delete)
        return
    
    # no key shortcut
    if not (eve.modifiers() & Qt.KeyboardModifier.ControlModifier or eve.modifiers() & Qt.KeyboardModifier.ShiftModifier): 
        lw('no any key or combination of keys')

