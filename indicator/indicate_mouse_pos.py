import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from value.strings import *

def indicate_mouse_pos(self: 'SLINE', pos: PointF) -> None:
    self.lb_pos.setText(POS_INDICATORf2.format(pos.x, pos.y))
    