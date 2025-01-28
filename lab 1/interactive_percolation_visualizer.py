import math
import turtle
from turtle_draw import enable_double_buffering, init_mouse_handler, clear, set_pen_color, set_xscale, set_yscale, filled_square, set_font, text, show, pause
from percolation import Percolation

DELAY = 20

def draw(perc, n):
    clear()
    set_xscale(-0.05 * n, 1.05 * n)
    set_yscale(-0.05 * n, 1.05 * n)

    size = 20
    opened = 0
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            x = col - 0.5
            y = n - row + 0.5
            if perc.is_full(row, col):
                filled_square(x, y, 0.60, "lightblue")
                opened += 1
            elif perc.is_open(row, col):
                filled_square(x, y, 0.60, "white")
                opened += 1
            else:
                filled_square(x, y, 0.60, "black")

    text(0.25 * n, -0.025 * n, f"{opened} open sites", "SansSerif", 12)
    if perc.percolates():
        text(0.75 * n, -0.025 * n, "percolates", "SansSerif", 12)
    else:
        text(0.75 * n, -0.025 * n, "does not percolate", "SansSerif", 12)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python interactive_percolation_visualizer.py n")
        return

    n = int(sys.argv[1]) if len(sys.argv) == 2 else 10
    print(n)

    enable_double_buffering()
    perc = Percolation(n)
    draw(perc, n)
    show()

    def on_mouse_click(x, y):
        i = int(n - math.floor(y))
        j = int(1 + math.floor(x))
        if 1 <= i <= n and 1 <= j <= n:
            if not perc.is_open(i, j):
                print(f"{i} {j}")
            perc.open(i, j)
            draw(perc, n)
            show()

    init_mouse_handler(on_mouse_click)

    while True:
        pause(DELAY)
        turtle.update()

if __name__ == "__main__":
    main()
