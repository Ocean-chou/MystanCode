"""
File: babygraphics.py
Name: Ocean
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    init_to_end = width-2*GRAPH_MARGIN_SIZE
    gap = init_to_end/(len(YEARS))
    x_coordinate = GRAPH_MARGIN_SIZE+gap*year_index
    return x_coordinate


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the name
    in the name_data dictionary, returns the y coordinate of the horizontal
    line associated with that year.

    Input:
        height (int): The height of the canvas
        rank (int): The rank of the name in the name_data dictionary
    Returns:
        y_coordinate (int): The y coordinate of the horizontal line associated
                            with the that year.
    """
    init_to_end = height-2*GRAPH_MARGIN_SIZE
    gap = init_to_end/MAX_RANK
    y_coordinate = GRAPH_MARGIN_SIZE+gap*int(rank)
    return y_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(0+GRAPH_MARGIN_SIZE, 0+GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, 0+GRAPH_MARGIN_SIZE)
    canvas.create_line(0+GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        year_index = i
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    n = 0
    for name in lookup_names:
        color = COLORS[n % len(COLORS)]     # The color will automatically change and cycle through COLORS list.
        n += 1
        info_dict = name_data[name]
        draw_line = False
        for i in range(len(YEARS)):
            year_index = i
            x = get_x_coordinate(CANVAS_WIDTH, year_index)
            if str(YEARS[i]) in info_dict:
                rank = info_dict[str(YEARS[i])]
                y = get_y_coordinate(CANVAS_HEIGHT, rank)
            else:
                rank = '*'
                y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_text(x + TEXT_DX, y, text=name + ' ' + rank, fill=color, anchor=tkinter.SW)
            # First point doesn't draw line, but we need to record x and y coordinate.
            if not draw_line:
                x1 = x
                y1 = y
                draw_line = True
            else:
            # Draw line and Record the x and y coordinate of point.
                canvas.create_line(x1, y1, x, y, width=LINE_WIDTH, fill=color)
                x1 = x
                y1 = y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
