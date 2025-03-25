from line_segment import LineSegment
from point import Point


class BruteCollinearPoints:
    def __init__(self, points: list[Point]):
        self.segments = []
        if points is None:
            raise ValueError("The list of points is None")
        for i in range(len(points)):
            if points[i] is None:
                raise ValueError("The list of points contains a None value")
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    raise ValueError("The list of points contains a repeated point")
                
        for p in points:
            for q in points:
                for r in points:
                    for s in points:
                        if p.slope_to(q) == p.slope_to(r) == p.slope_to(s):
                            self.segments.append(LineSegment(p, s))
        

    def number_of_segments(self) -> int:
        return len(self.segments)

    def segments(self) -> list[LineSegment]:
        return self.segments