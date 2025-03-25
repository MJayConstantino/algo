from __future__ import annotations
from point import Point

import turtle


class LineSegment:
    def __init__(self, p: Point, q: Point):
        # DO NOT MODIFY
        self.p = p
        self.q = q

    def draw(self) -> None:
        # DO NOT MODIFY
        turtle.penup()
        turtle.goto(self.p.x, self.p.y)
        turtle.pendown()
        turtle.pensize(2)
        turtle.pencolor("black")
        turtle.goto(self.q.x, self.q.y)

    def __str__(self) -> str:
        # DO NOT MODIFY
        return f"{self.p} -> {self.q}"

    @staticmethod
    def main():
        LENGTH = 800
        WIDTH = 600
        MARGIN = 50

        # Initialize turtle screen
        screen = turtle.Screen()
        screen.setup(LENGTH, WIDTH)

        # Transfer the point of origin to the bottom left
        screen.setworldcoordinates(-MARGIN, -MARGIN, LENGTH - MARGIN, WIDTH - MARGIN)
        turtle.hideturtle()

        # Create points
        p1 = Point(50, 100)
        p2 = Point(150, 200)

        # Create a line segment
        line = LineSegment(p1, p2)

        # Draw the line segment
        line.draw()

        # Keep the window open
        turtle.done()


# Example usage
if __name__ == "__main__":
    LineSegment.main()
