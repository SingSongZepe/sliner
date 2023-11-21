import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.rect import RectF
from sszp.sszpgraphics_rect import SSZPGraphicsRect

def draw_rect(self: 'SLINE', rect: RectF) -> SSZPGraphicsRect:
    rect_item = SSZPGraphicsRect(rect)
    self.gv_graphics.scene().addItem(rect_item)
    return rect_item
