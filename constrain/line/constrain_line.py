import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.line import LineF
from object.constrained import ConstrainCondition, ConstrainedPoint

def constrain_line(self: 'SLINE', point: PointF) -> ConstrainedPoint:
    # select current point
    # Priority 0 (current point)
    if self.graphics_points.near_a_point(point):
        return ConstrainedPoint(self.graphics_points.near_which_point(point), ConstrainCondition.CurrentPoint)

    # Priority 1 (vhp)
    if self.selected_graphics_object.for_assist_line():  # one 
        # selected point
        p: PointF = self.selected_graphics_object.all()[0]
        # perpendicular must in line
        # it's subpriority higher then just horizon or vertical
        if line := self.graphics_lines.perpendicular_which_line(LineF(p, point)):
            return ConstrainedPoint(line.get_perpendicular_point(p), ConstrainCondition.Perpendicular, [line])
        if line := self.graphics_lines.parallel_which_line(LineF(p, point)):
            for p_ in line.points:
                if line.perpendicular(LineF(point, p_)):
                    return ConstrainedPoint(line.get_parallel_isolength_point(p_, p), ConstrainCondition.ParallelIsoLength, [line, p_])
            return ConstrainedPoint(line.get_parallel_point(p, point), ConstrainCondition.Parallel, [line])
        
        if p.horizontal(point):
            # if horizontal and in line
            if l := self.graphics_lines.near_which_line(point):
                if p_ := l.get_horizontal_point(p):
                    return ConstrainedPoint(PointF(p_.x, p.y), ConstrainCondition.HorizontalInLine)
            return ConstrainedPoint(PointF(point.x, p.y), ConstrainCondition.Horizontal)
        elif p.vertical(point):
            if l := self.graphics_lines.near_which_line(point):
                if p_ := l.get_vertical_point(p):
                    return ConstrainedPoint(PointF(p.x, p_.y), ConstrainCondition.VerticalInLine)
            return ConstrainedPoint(PointF(p.x, point.y), ConstrainCondition.Vertical)

    # Priority 2 (in line)
    if line := self.graphics_lines.near_which_line(point):
        return ConstrainedPoint(line.get_perpendicular_point(point), ConstrainCondition.InLine, [line])
    
    # Priority 3 (angle when no target)
    if self.selected_graphics_object.for_assist_line():  # one 
        # selected point
        p: PointF = self.selected_graphics_object.all()[0]
        # line p-point
        return ConstrainedPoint(LineF(p, point).get_integer_ang_point(), ConstrainCondition.AngleToHV)

    # Priority 4


    # Priority n (all point)
    return ConstrainedPoint(point, ConstrainCondition.None_)

