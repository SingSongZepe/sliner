
from object.point import PointF
from object.color import Color
from value.value import *
from value.strings import *

from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QGraphicsItem

class SSZPGraphicsPoint(QGraphicsItem):
    def __init__(self, point: PointF, size=POINT_SIZE, color=default_color):
        super().__init__()
        self.size = size
        self.color = color
        self.point = point
        self.pen = QPen(self.color)
        self.brush = QBrush(self.color)
        self.pen.setWidth(2)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        return QRectF(QPointF(self.point.x-self.size/2, self.point.y-self.size/2), QPointF(self.point.x+self.size/2, self.point.y+self.size/2)).normalized()

    def paint(self, painter, option, widget=None):
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawLine(QPointF(self.point.x-self.size/2, self.point.y-self.size/2), QPointF(self.point.x+self.size/2, self.point.y+self.size/2))
        painter.drawLine(QPointF(self.point.x+self.size/2, self.point.y-self.size/2), QPointF(self.point.x-self.size/2, self.point.y+self.size/2))

    # provided function
    def change_color(self, new_color: Qt.GlobalColor):
        self.color = new_color
        self.pen.setColor(self.color)
        self.brush.setColor(self.color)
        self.update()