import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from sszp.sszpgraphics_point import SSZPGraphicsPoint

def draw_point(self: 'SLINE', point: PointF) -> SSZPGraphicsPoint:
    point_item = SSZPGraphicsPoint(point)
    self.gv_graphics.scene().addItem(point_item)
    return point_item

    # point = QGraphicsEllipseItem(point.x - radius_point, point.y - radius_point, 2 * radius_point, 2 * radius_point)
    # # set color
    # point.setBrush(Qt.GlobalColor.black)
    # self.gv_graphics.scene().addItem(point)
    # return point
