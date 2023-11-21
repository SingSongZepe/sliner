
from object.point import PointF
from object.rect import RectF
from value.value import *
from value.strings import *

from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QGraphicsItem

class SSZPGraphicsRect(QGraphicsItem):
    def __init__(self, rect: RectF, size=POINT_SIZE, color=default_color):
        super().__init__()
        self.size = size
        self.color = color
        self._rect = rect
        self.cal_points()
        self.pen = QPen(self.color)
        self.brush = QBrush(self.color)
        self.pen.setWidth(2)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, new_rect: RectF):
        self._rect = new_rect
        # recalculate the p1 p2 p3 p4 
        self.cal_points()

    # self cal
    def cal_points(self):
        self.p1 = self._rect.p1
        self.p2 = self._rect.p2
        self.p3 = PointF(self.p2.x, self.p1.y)
        self.p4 = PointF(self.p1.x, self.p2.y)

    def boundingRect(self):
        return QRectF(self.p1.to_QPointF(), self.p2.to_QPointF()).normalized().adjusted(-self.size/2, -self.size/2, self.size/2, self.size/2)
    
    def paint(self, painter, option, widget=None):
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawLine(QPointF(self.p1.x, self.p1.y), QPointF(self.p3.x, self.p3.y))
        painter.drawLine(QPointF(self.p1.x, self.p1.y), QPointF(self.p4.x, self.p4.y))
        painter.drawLine(QPointF(self.p2.x, self.p2.y), QPointF(self.p3.x, self.p3.y))
        painter.drawLine(QPointF(self.p2.x, self.p2.y), QPointF(self.p4.x, self.p4.y))

        # there be draw point in the vertex of rect, but it may make user thinks that the edge of the rect is a line and selectable
        #     # p1 vertex
        # painter.drawLine(QPointF(self.p1.x-self.size/2, self.p1.y-self.size/2), QPointF(self.p1.x+self.size/2, self.p1.y+self.size/2))
        # painter.drawLine(QPointF(self.p1.x+self.size/2, self.p1.y-self.size/2), QPointF(self.p1.x-self.size/2, self.p1.y+self.size/2))
        #     # p2 vertex
        # painter.drawLine(QPointF(self.p2.x-self.size/2, self.p2.y-self.size/2), QPointF(self.p2.x+self.size/2, self.p2.y+self.size/2))
        # painter.drawLine(QPointF(self.p2.x+self.size/2, self.p2.y-self.size/2), QPointF(self.p2.x-self.size/2, self.p2.y+self.size/2))
        #     # p3 vertex
        # painter.drawLine(QPointF(self.p3.x-self.size/2, self.p3.y-self.size/2), QPointF(self.p3.x+self.size/2, self.p3.y+self.size/2))
        # painter.drawLine(QPointF(self.p3.x+self.size/2, self.p3.y-self.size/2), QPointF(self.p3.x-self.size/2, self.p3.y+self.size/2))
        #     # p4 vertex
        # painter.drawLine(QPointF(self.p4.x-self.size/2, self.p4.y-self.size/2), QPointF(self.p4.x+self.size/2, self.p4.y+self.size/2))
        # painter.drawLine(QPointF(self.p4.x+self.size/2, self.p4.y-self.size/2), QPointF(self.p4.x-self.size/2, self.p4.y+self.size/2))
    
    # provided function
    def change_color(self, new_color: Qt.GlobalColor):
        self.color = new_color
        self.pen.setColor(self.color)
        self.brush.setColor(self.color)
        self.update()



