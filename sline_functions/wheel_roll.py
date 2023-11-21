import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from value.value import *

from PySide6.QtGui import QWheelEvent

def wheel_roll(self: 'SLINE', eve: QWheelEvent) -> None:
    angle = eve.angleDelta().y()
    if angle < 0:
        factors = 1.0 / WHEEL_ROLLS_FACTORS
        self.gv_graphics.scale(factors, factors)
    if angle > 0:
        factors = WHEEL_ROLLS_FACTORS / 1.0
        self.gv_graphics.scale(factors, factors)



