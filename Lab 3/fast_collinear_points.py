from __future__ import annotations
from line_segment import LineSegment
from point import Point

class FastCollinearPoints:
    def __init__(self, points: list[Point]):
        if points is None:
            raise ValueError("The list of points is None")
        
        self.points = points.copy()
        self.sorted_points = sorted(self.points)
        self._validate_points(self.sorted_points)
        self._segments: list[LineSegment] = None

    def _validate_points(self, points: list[Point]) -> None:
        for pt in points:
            if pt is None:
                raise ValueError("The list of points contains a None value")
        
        for i in range(1, len(points)):
            if points[i] == points[i - 1]:
                raise ValueError("The list of points contains a repeated point")

    def segments(self) -> list[LineSegment]:
        if self._segments is not None:
            return self._segments.copy()
        
        segments = []

        for p_origin in self.sorted_points:
            # Sort all points by the slope they make with p_origin
            points_by_slope = sorted(self.sorted_points, key=lambda point: p_origin.slope_to(point))

            j = 1  
            while j < len(points_by_slope):
                collinear = [points_by_slope[j]]
                slope_ref = p_origin.slope_to(points_by_slope[j])
                j += 1

                # Group points with the same slope
                while j < len(points_by_slope) and p_origin.slope_to(points_by_slope[j]) == slope_ref:
                    collinear.append(points_by_slope[j])
                    j += 1

                if len(collinear) >= 3:
                    candidate = [p_origin] + collinear
                    candidate.sort()

                    if candidate[0] == p_origin:
                        segments.append(LineSegment(candidate[0], candidate[-1]))

        self._segments = segments
        return segments.copy()

    def number_of_segments(self) -> int:
        return len(self.segments())
