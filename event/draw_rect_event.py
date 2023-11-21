
from object.rect import RectF
from event.draw_event import DrawEvent
from sszp.sszpgraphics_rect import SSZPGraphicsRect


class DrawRectEvent(DrawEvent):
    def __init__(self, rect: RectF, item: SSZPGraphicsRect):
        self.rect = rect
        self.item = item


