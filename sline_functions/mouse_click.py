import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.mode import Mode
from object.point import PointF

from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

def mouse_click(self: 'SLINE', eve: QMouseEvent) -> None:
    pos = eve.pos()
    spos = self.gv_graphics.mapToScene(pos)
    point = PointF(spos.x(), spos.y())

    # Delete
    if Mode.eq(self.mode, Mode.Delete):
        if p := self.select_point(point):
            if draw_point_event := self.undo_stack.get_event(p):
                # change it color to selected_color
                self.selected_events.append(draw_point_event)
                delete_event_event = self.delete_event()
                self.undo_stack.append(delete_event_event)
                return
        elif l := self.select_line(point):
            if draw_line_event := self.undo_stack.get_event(l):
                self.selected_events.append(draw_line_event)
                delete_event_event = self.delete_event()
                self.undo_stack.append(delete_event_event)
                return

    # translating
    if Mode.eq(self.mode, Mode.Emp):
        # rect select
        if eve.button() == Qt.MouseButton.LeftButton and not eve.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self._rect_select = True
            self._rect_select_start_pos = point
            # return means it is unnecessary to clear redo_stack
            return
        # translate
        elif eve.button() == Qt.MouseButton.LeftButton and eve.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self._tran = True
            self._tran_start_pos = point
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            # return means it is unnecessary to clear redo_stack
            return

    # draw
    if Mode.eq(self.mode, Mode.Point):
        self.process_point(point)
    elif Mode.eq(self.mode, Mode.Line):
        self.process_line(point)
    elif Mode.eq(self.mode, Mode.Trim):
        self.process_trim(point)

    self.redo_stack.cls()



