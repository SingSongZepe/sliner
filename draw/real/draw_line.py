import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from sszp.sszpgraphics_line import SSZPGraphicsLine

def draw_line(self: 'SLINE', p1: PointF, p2: PointF) -> SSZPGraphicsLine:
    line_item = SSZPGraphicsLine(p1, p2)
    self.gv_graphics.scene().addItem(line_item)
    return line_item
