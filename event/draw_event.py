
from sszp.sszpgraphics_line import SSZPGraphicsLine
from sszp.sszpgraphics_point import SSZPGraphicsPoint
from sszp.sszpgraphics_rect import SSZPGraphicsRect

from PySide6.QtWidgets import QGraphicsItem
from PySide6.QtCore import Qt

class DrawEvent:
    def __init__(self, item: QGraphicsItem) -> None:
        self.item: SSZPGraphicsLine | SSZPGraphicsPoint | SSZPGraphicsRect  = item
