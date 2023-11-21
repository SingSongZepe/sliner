import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from sszp.sszpgraphics_line import SSZPGraphicsLine

def draw_assist_line(self: 'SLINE', p1: PointF, p2: PointF) -> SSZPGraphicsLine:
    # there may be use dashline
    return self.draw_line(p1, p2)

