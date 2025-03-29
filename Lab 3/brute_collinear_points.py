from line_segment import LineSegment
from point import Point


class BruteCollinearPoints:
    def __init__(self, points: list[Point]):
        self._segments: list[LineSegment] = []

        if points is None:
            raise ValueError("The list of points is None")
        
        for i in range(len(points)):
            if points[i] is None:
                raise ValueError("The list of points contains a None value")
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    raise ValueError("The list of points contains a repeated point")
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    for l in range(k + 1, len(points)):
                        p, q, r, s = points[i], points[j], points[k], points[l]
                        if p.slope_to(q) == p.slope_to(r) == p.slope_to(s):
                            endpoints = sorted([p, q, r, s])
                            self._segments.append(LineSegment(endpoints[0], endpoints[-1]))

    def number_of_segments(self) -> int:
        return len(self._segments)

    def segments(self) -> list[LineSegment]:
        return self._segments