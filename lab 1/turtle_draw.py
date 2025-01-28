import turtle

def enable_double_buffering():
    turtle.setup(width=600, height=600)
    turtle.tracer(0, 0)

def init_mouse_handler(on_mouse_click):
    turtle.onscreenclick(on_mouse_click)

def clear():
    turtle.clear()

def set_pen_color(color):
    turtle.pencolor(color)

def set_xscale(start, end):
    turtle.setworldcoordinates(start, start, end, end)

def set_yscale(start, end):
    turtle.setworldcoordinates(start, start, end, end)

def filled_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x - size / 2, y - size / 2)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

def set_font(fontname, fontsize):
    turtle.write('', font=(fontname, fontsize))

def text(x, y, text, fontname="SansSerif", fontsize=12):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, font=(fontname, fontsize))

def show():
    turtle.update()

def pause(delay):
    turtle.ontimer(lambda: None, delay)
