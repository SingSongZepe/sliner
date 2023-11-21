
from object.line import LineF
from event.draw_event import DrawEvent
from sszp.sszpgraphics_line import SSZPGraphicsLine

class DrawLineEvent(DrawEvent):

    # this line is stored in graphics_lines

    def __init__(self, line: LineF, item: SSZPGraphicsLine):
        self.line = line
        self.item = item
