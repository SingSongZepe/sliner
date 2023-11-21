import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.line import LineF
from object.point import PointF
from event.draw_line_event import DrawLineEvent

def process_line(self: 'SLINE', point: PointF):
    # select point, appending to graphics_points
    constrained_point = self.constrain_line(point)
    point = constrained_point.point
    
    if self.graphics_points.exist(point):
        point = self.graphics_points.get(point)
        self.selected_graphics_object.append(point)
    else:
        self.graphics_points.append(point)
        point_item = self.draw_point(point)
        # for drawing a line, it assist draw point event is not a event that needed to append
        # self.undo_stack.append(DrawPointEvent(point, point_item))
        self.selected_graphics_object.append(point)
        self.selected_graphics_item.append(point_item)

    # meet the condition to draw a line
    if self.selected_graphics_object.for_line():
        if points := self.selected_graphics_object.get_objects(2):
            line = LineF(points[0], points[1])
            line_item = self.draw_line(points[0], points[1])
            self.undo_stack.append(DrawLineEvent(line, line_item))
            self.graphics_lines.append(line)

            # clear the select_graphics_object
            self.selected_graphics_object.cls()
            for item in self.selected_graphics_item.all():
                self.gv_graphics.scene().removeItem(item)
            self.selected_graphics_item.cls()
