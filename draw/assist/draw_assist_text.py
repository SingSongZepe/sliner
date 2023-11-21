import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from value.strings import *

from PySide6.QtWidgets import QGraphicsTextItem


def draw_assist_horizontal(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return self.draw_horizontal(point)

def draw_assist_vertical(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return self.draw_vertical(point)

def draw_assist_perpendicular(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return self.draw_perpendicular(point)

def draw_assist_parallel(self: 'SLINE', point: PointF) -> QGraphicsTextItem:
    return self.draw_parallel(point)

def draw_assist_line_info(self: 'SLINE', point: PointF) -> typing.List[QGraphicsTextItem] | bool:
    return self.draw_line_info(point)

