import typing

if typing.TYPE_CHECKING:
    from sline import SLINE

from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

def mouse_release(self: 'SLINE', eve: QMouseEvent):
    
    if self._tran:
        self._tran = False
        self.setCursor(Qt.CursorShape.ArrowCursor)
    if self._rect_select:
        self._rect_select = False
        
