import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.rect import RectF
from sszp.sszpgraphics_rect import SSZPGraphicsRect

def draw_assist_rect(self: 'SLINE', rect: RectF) -> SSZPGraphicsRect:
    return self.draw_rect(rect)

