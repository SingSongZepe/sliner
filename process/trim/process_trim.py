import typing

if typing.TYPE_CHECKING:
    from sline import SLINE
from object.point import PointF
from object.line import LineF

from event.draw_line_event import DrawLineEvent
from event.trim_event import TrimEvent
from utils.common.log import *

def process_trim(self: 'SLINE', point: PointF):
    if line := self.graphics_lines.near_which_line(point):
        intersect_points = self.graphics_lines.intersect_point_list(line)
        # there be a point in the list
        if intersect_points:
            if not any(line.p1 == p for p in intersect_points):
                intersect_points.insert(0, line.p1)
            if not any(line.p2 == p for p in intersect_points):
                intersect_points.insert(len(intersect_points), line.p2)

            # from p1 or p2
            tp_ = None
            bp_ = None
            # vertical judgement when vertical use its y and when horizontal use its x
            if line.vertical():
                if line.p1.y > line.p2.y:
                    tpoint = line.p1
                    bpoint = line.p2
                else:
                    tpoint = line.p2
                    bpoint = line.p1
                tp_ = tpoint
                bp_ = bpoint
                for p in intersect_points:
                    if p.y > bpoint.y and p.y < point.y:
                        bpoint = p
                    elif p.y < tpoint.y and p.y > point.y:
                        tpoint = p
            # common case
            else:
                if line.p1.x > line.p2.x:
                    tpoint = line.p1
                    bpoint = line.p2
                else:
                    tpoint = line.p2
                    bpoint = line.p1
                tp_ = tpoint
                bp_ = bpoint
                for p in intersect_points:
                    if p.x > bpoint.x and p.x < point.x:
                        bpoint = p
                    elif p.x < tpoint.x and p.x > point.x:
                        tpoint = p
            # position found
            
            draw_line_event = self.undo_stack.get_event(line)
            # append
            self.selected_events.append(draw_line_event)
            delete_event_event = self.delete_event()
            draw_events = []
            if tpoint != tp_:
                line_item = self.draw_line(tpoint, tp_)
                line = LineF(tpoint, tp_)
                draw_events.append(DrawLineEvent(line, line_item))
                self.graphics_lines.append(line)
                
                # draw line, don't draw_point, but add its point into the graphics_points
                self.graphics_points.append(tpoint)
            if bpoint != bp_:
                line_item = self.draw_line(bpoint, bp_)
                line = LineF(bpoint, bp_)
                draw_events.append(DrawLineEvent(line, line_item))
                self.graphics_lines.append(line)

                # draw line, don't draw_point, but add its point into the graphics_points
                self.graphics_points.append(bpoint)
            for draw_line_event in draw_events:
                self.undo_stack.append(draw_line_event)
            trim_event = TrimEvent(
                delete_event_event=delete_event_event,
                draw_events=draw_events,
            )
            self.undo_stack.append(trim_event)

        else:
            lw('no any line intersect with the line that you selected')



