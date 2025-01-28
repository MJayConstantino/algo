import time
import turtle
from lib.in_lib import In
from percolation import Percolation

# DELAY = 100


def draw_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def draw(perc: Percolation, n):
    turtle.clear()
    turtle.hideturtle()
    turtle.speed(0)

    # draw n-by-n grid
    opened = 0
    size = 320 // n
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            x = (col - 1) * size - (n * size) / 2
            # y = ((n - row) * size - (n * size) / 2)
            y = (n - row) * size - size / 2
            if perc.is_full(row, col):
                draw_square(x, y, size, 'lightblue')
                opened += 1
            elif perc.is_open(row, col):
                draw_square(x, y, size, 'white')
                opened += 1
            else:
                draw_square(x, y, size, 'black')

    # write status text
    turtle.penup()
    turtle.goto(-(n+2) * size / 2, -4 * size / 2 - 20)
    turtle.pendown()
    turtle.write(f"{opened} open sites", font=("SansSerif", 12, "normal"))
    turtle.penup()
    turtle.goto((n+2) * size / 2, -4 * size / 2 - 20)
    turtle.pendown()
    if perc.percolates():
        turtle.write("percolates", align="right",
                     font=("SansSerif", 12, "normal"))
    else:
        turtle.write("does not percolate", align="right",
                     font=("SansSerif", 12, "normal"))


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python percolation_visualizer.py input.txt")
        return

    filename = sys.argv[1]
    infile = In(filename)
    n = infile.read_int()

    perc = Percolation(n)
    turtle.setup(width=600, height=600)
    turtle.tracer(False)

    draw(perc, n)
    turtle.update()
    # time.sleep(DELAY / 1000.0)

    while not infile.is_empty():
        i = infile.read_int()
        j = infile.read_int()
        perc.open(i, j)
        draw(perc, n)
        turtle.update()
        # time.sleep(DELAY / 1000.0)

    turtle.done()


if __name__ == "__main__":
    main()
