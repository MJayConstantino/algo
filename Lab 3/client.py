import turtle

from fast_collinear_points import FastCollinearPoints
from point import Point
from sys import argv


# Main program
def main(filename):
    # Read points from file
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().strip().split())
            points.append(Point(x, y))

    # Draw the points
    LENGTH = 32678
    WIDTH = 32678

    # Initialize turtle screen
    screen = turtle.Screen()
    screen.setup(LENGTH, WIDTH)

    # Transfer the point of origin to the bottom left
    turtle.setworldcoordinates(0, 0, LENGTH, WIDTH)
    turtle.hideturtle()

    for p in points:
        p.draw()

    # Print and draw the line segments
    collinear = FastCollinearPoints(points)
    for segment in collinear.segments():
        print(f"{segment.p} -> {segment.q}")
        segment.draw()

    turtle.done()


if __name__ == "__main__":
    # Call this file with `python client.py <txt_file_name>`
    # e.g. python client.py input.txt
    main(argv[1])