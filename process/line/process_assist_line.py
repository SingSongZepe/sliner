import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.constrained import ConstrainCondition

def process_assist_line(self: 'SLINE', point: PointF) -> None:
    constrained_point = self.constrain_line(point)
    point = constrained_point.point

    # process constrain
    if constrained_point.condition == ConstrainCondition.Horizontal or constrained_point.condition == ConstrainCondition.HorizontalInLine:
        # there must exist a point in sgo and it is the a PointF object
        text_assist_item = self.draw_assist_horizontal((self.selected_graphics_object.all()[0] + point) / 2)
        self.assist_graphics_item.append(text_assist_item)
    elif constrained_point.condition == ConstrainCondition.Vertical or constrained_point.condition == ConstrainCondition.VerticalInLine:
        text_assist_item = self.draw_assist_vertical((self.selected_graphics_object.all()[0] + point) / 2)
        self.assist_graphics_item.append(text_assist_item)
    elif constrained_point.condition == ConstrainCondition.InLine:
        point_assist_item = self.draw_assist_point(point)
        self.assist_graphics_item.append(point_assist_item)
    elif constrained_point.condition == ConstrainCondition.Perpendicular:
        text_assist_item = self.draw_assist_perpendicular((self.selected_graphics_object.all()[0] + point) / 2)
        self.assist_graphics_item.append(text_assist_item)
    elif constrained_point.condition == ConstrainCondition.Parallel:
        text_assist_item = self.draw_assist_parallel((self.selected_graphics_object.all()[0] + point) / 2)
        self.assist_graphics_item.append(text_assist_item)

    # meet the condition of constructing a assist line
    if self.selected_graphics_object.for_assist_line():
        line_assist_item = self.draw_assist_line(self.selected_graphics_object.all()[0], point)
        self.assist_graphics_item.append(line_assist_item)
    
    if self.selected_graphics_object.for_assist_line_info():
        if (text_assist_item := self.draw_assist_line_info(point)) and text_assist_item[0]:
            for item in text_assist_item:
                self.assist_graphics_item.append(item)
