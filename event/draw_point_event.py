
from object.point import PointF
from event.draw_event import DrawEvent
from sszp.sszpgraphics_point import SSZPGraphicsPoint

class DrawPointEvent(DrawEvent):

    # this point is stored in graphics_points

    def __init__(self, point: PointF, item: SSZPGraphicsPoint):
        self.point = point
        self.item = item


