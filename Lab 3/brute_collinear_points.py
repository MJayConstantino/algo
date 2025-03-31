from line_segment import LineSegment
from point import Point


class BruteCollinearPoints:
    def __init__(self, points: list[Point]):
        self._segments: list[LineSegment] = []
        if points is None:
            raise ValueError("The list of points is None")
    
        points_copy = points.copy()
        for i in range(len(points_copy)):
            if points_copy[i] is None:
                raise ValueError("The list of points contains a None value")
            for j in range(i + 1, len(points_copy)):
                if points_copy[i] == points_copy[j]:
                    raise ValueError("The list of points contains a repeated point")
                
        lines_found = set()
        n = len(points_copy)
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        p, q, r, s = points_copy[i], points_copy[j], points_copy[k], points_copy[l]
                        
                        slope1 = p.slope_to(q)
                        slope2 = p.slope_to(r)
                        slope3 = p.slope_to(s)
                        
                        if slope1 == slope2 == slope3:

                            collinear_points = [p, q, r, s]
                            collinear_points.sort()
                            
                            min_point = collinear_points[0]
                            max_point = collinear_points[-1]
                            line_key = (min_point.x, min_point.y, max_point.x, max_point.y)
                            
                            if line_key not in lines_found:
                                lines_found.add(line_key)
                                self._segments.append(LineSegment(min_point, max_point))
    
    def number_of_segments(self) -> int:
        return len(self._segments)
    
    def segments(self) -> list[LineSegment]:
        return self._segments.copy()
