import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from value.value import *
from sszp.sszpgraphics_point import SSZPGraphicsPoint

from PySide6.QtWidgets import QGraphicsItem
from PySide6.QtCore import Qt

def draw_assist_point(self: 'SLINE', point: PointF) -> QGraphicsItem:
    point = SSZPGraphicsPoint(point, size=POINT_SIZE, color=Qt.GlobalColor.gray)
    self.gv_graphics.scene().addItem(point)
    return point

