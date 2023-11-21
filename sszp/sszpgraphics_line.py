from typing import overload

from object.point import PointF
from object.line import LineF
from value.value import *
from value.strings import *
from err.parameter import ParameterNotCorrectError

from PySide6.QtWidgets import QGraphicsLineItem
from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtGui import QPainter, QPen

class SSZPGraphicsLine(QGraphicsLineItem):
    @overload
    def __init__(self, line: LineF) -> None:
        ...
    @overload
    def __init__(self, p1: PointF, p2: PointF):
        ...
    @overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        ...
    def __init__(self, *args) -> None:
        super().__init__()
        self.setFlag(QGraphicsLineItem.ItemIsMovable, True)
        self.setFlag(QGraphicsLineItem.ItemSendsGeometryChanges, True)
        self.size = POINT_SIZE
        self.color = default_color
        self.pen_ = QPen(self.color)
        if len(args) == 1:
            self.p1 = QPointF(args[0].p1.x, args[0].p1.y)
            self.p2 = QPointF(args[0].p2.x, args[0].p2.y)
        elif len(args) == 2:
            self.p1 = QPointF(args[0].x, args[0].y)
            self.p2 = QPointF(args[1].x, args[1].y)
            return
        elif len(args) == 4:
            self.p1 = QPointF(args[0], args[1])
            self.p2 = QPointF(args[2], args[3])
            return
        else:
            raise ParameterNotCorrectError('error number of arguments not correct')

    def boundingRect(self) -> QRectF:
        return QRectF(self.p1, self.p2).normalized().adjusted(-self.size/2, -self.size/2, self.size/2, self.size/2)
    
    def paint(self, painter: QPainter, _, __) -> None:
        painter.setPen(self.pen_)
        # painter.setBrush(QBrush(Qt.GlobalColor.black))
        painter.drawLine(self.p1, self.p2)
        painter.drawLine(QPointF(self.p1.x()-self.size/2, self.p1.y()-self.size/2), QPointF(self.p1.x()+self.size/2, self.p1.y()+self.size/2))
        painter.drawLine(QPointF(self.p1.x()+self.size/2, self.p1.y()-self.size/2), QPointF(self.p1.x()-self.size/2, self.p1.y()+self.size/2))
        painter.drawLine(QPointF(self.p2.x()-self.size/2, self.p2.y()-self.size/2), QPointF(self.p2.x()+self.size/2, self.p2.y()+self.size/2))
        painter.drawLine(QPointF(self.p2.x()+self.size/2, self.p2.y()-self.size/2), QPointF(self.p2.x()-self.size/2, self.p2.y()+self.size/2))

    def itemChange(self, change, value):
        if change == QGraphicsLineItem.ItemPositionChange:
            delta = value - self.pos()
            self.p1 += delta
            self.p2 += delta
        return super().itemChange(change, value)

    def change_color(self, new_color: Qt.GlobalColor):
        self.color = new_color
        self.pen_ = QPen(self.color)
        self.update()


