import turtle
from fast_collinear_points import FastCollinearPoints
from brute_collinear_points import BruteCollinearPoints
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

    # Get bounds of the points
    min_x = min(p.x for p in points) if points else 0
    min_y = min(p.y for p in points) if points else 0
    max_x = max(p.x for p in points) if points else 32678
    max_y = max(p.y for p in points) if points else 32678

    # Add margin
    MARGIN_PERCENT = 0.1
    width = max(1, max_x - min_x)  # Ensure non-zero width
    height = max(1, max_y - min_y)  # Ensure non-zero height

    margin_x = width * MARGIN_PERCENT
    margin_y = height * MARGIN_PERCENT

    view_min_x = max(0, min_x - margin_x)
    view_min_y = max(0, min_y - margin_y)
    view_max_x = min(32678, max_x + margin_x)
    view_max_y = min(32678, max_y + margin_y)

    # Get screen dimensions that comfortably fit on most displays
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800

    # Initialize turtle screen
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(f"Collinear Points from {filename}")

    # Set the coordinate system to match the data bounds
    turtle.setworldcoordinates(view_min_x, view_min_y, view_max_x, view_max_y)
    turtle.hideturtle()
    turtle.speed(0)  # Fastest drawing speed

    # Draw the points
    for p in points:
        p.draw()

    # Print and draw the line segments
    collinear = BruteCollinearPoints(points)
    for segment in collinear.segments():
        print(f"{segment.p} -> {segment.q}")
        segment.draw()

    turtle.done()


if __name__ == "__main__":
    # Call this file with `python client.py <txt_file_name>`
    # e.g. python client.py input.txt
    main(argv[1])