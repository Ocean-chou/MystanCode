"""
File: draw_line.py
Name: Ocean
-------------------------
This file uses the campy mouse event to draw line.
When click count is odd, the program generates a circle at mouse position.
When it's even, it produces a line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 20
window = GWindow()
click = 0
obj = window.get_object_at(0, 0)
line = False


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global click
    global obj
    global line
    click += 1
    circle = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
    if line is False:
        window.add(circle)
        obj = window.get_object_at(circle.x + SIZE / 2, circle.y + SIZE / 2)
        line = True
    else:
        draw_line = GLine(obj.x + SIZE / 2, obj.y + SIZE / 2, mouse.x, mouse.y)
        window.add(draw_line)
        window.remove(obj)
        line = False


    # if click % 2 == 1:
    #     # When the click count is odd, the program generates a circle.
    #     window.add(circle)
    #     obj = window.get_object_at(circle.x+SIZE/2, circle.y+SIZE/2)
    # else:
    #     # When the click count is even, the program generates a line, and remove the circle generated previously.
    #     line = GLine(obj.x+SIZE/2, obj.y+SIZE/2, mouse.x, mouse.y)
    #     window.add(line)
    #     window.remove(obj)


if __name__ == "__main__":
    main()
