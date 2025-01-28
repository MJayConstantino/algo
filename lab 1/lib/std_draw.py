import matplotlib.pyplot as plt
import matplotlib.patches as patches

class StdDraw:
    mouse_pressed = False
    mouse_x = 0
    mouse_y = 0
    
    @staticmethod
    def on_mouse_press(event):
        if event.inaxes:
            StdDraw.mouse_pressed = True
            StdDraw.mouse_x, StdDraw.mouse_y = event.xdata, event.ydata

    @staticmethod
    def enable_double_buffering():
        plt.ion()
    
    @staticmethod
    def clear():
        plt.clf()
    
    @staticmethod
    def set_pen_color(color):
        plt.gca().set_facecolor(color)
    
    @staticmethod
    def set_xscale(start, end):
        plt.xlim(start, end)
    
    @staticmethod
    def set_yscale(start, end):
        plt.ylim(start, end)
    
    @staticmethod
    def filled_square(x, y, radius, color='black'):
        square = patches.Rectangle((x - radius, y - radius), 2*radius, 2*radius, color=color)
        plt.gca().add_patch(square)
    
    @staticmethod
    def set_font(fontname, fontsize):
        plt.rcParams.update({'font.size': fontsize})
    
    @staticmethod
    def text(x, y, text):
        plt.text(x, y, text, horizontalalignment='center')
    
    @staticmethod
    def show():
        plt.draw()
        plt.pause(0.001)
    
    @staticmethod
    def pause(delay):
        plt.pause(delay / 1000)
    
    @staticmethod
    def is_mouse_pressed():
        return StdDraw.mouse_pressed
    
    @staticmethod
    def mouseX():
        return StdDraw.mouse_x
    
    @staticmethod
    def mouseY():
        return StdDraw.mouse_y
    
    @staticmethod
    def reset_mouse():
        StdDraw.mouse_pressed = False

    @staticmethod
    def init_mouse_handler():
        plt.gcf().canvas.mpl_connect('button_press_event', StdDraw.on_mouse_press)
