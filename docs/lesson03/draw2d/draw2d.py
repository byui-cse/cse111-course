# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
This is a library of drawing functions used by BYU-Idaho CSE 111
students to complete an assignment that draws an outdoor scene to a
window. The intent of the assignment is to teach students to separate a
large program into functions with parameters.

The functions in this library are simply wrapper functions that create
and use tkinter objects. The benefits provided by these wrapper
functions are as follows:
1. Elminate the need for students' code to call object-oriented canvas
   methods. Students' code calls functions instead of methods.
2. Simplify the options available to only those needed to complete the
   CSE 111 assignment.
3. Include type and value checking for the parameters passed to tkinter.

Advantages of tkinter over kivy
1. tkinter is installed as part of Python.
2. With tkinter colors are passed as part of the calls to create_oval,
   create_line, create_polygon, etc. which makes more sense to students
   than kivy where they are added to the canvas before a shape is added.
"""

from tkinter import Tk, Frame, Canvas, BOTH
from numbers import Number

_started = False


def start_drawing(title, width, height):
    """Create a window with a canvas where a program can draw
    2-dimensional shapes.

    Parameters
        title: the title that will appear in the frame's title bar
        width: the width in pixels of the canvas
        height: the height in pixels of the canvas
    Return: the new canvas
    """
    global _started
    assert not _started, "your program must call start_drawing once only"
    assert isinstance(title, str), _wrong_type(title, "title", "string")
    min_width = 100
    min_height = 100
    assert isinstance(width, Number), \
        _wrong_type_2(width, "width", "number", min_width)
    assert isinstance(height, Number), \
        _wrong_type_2(height, "height", "number", min_height)
    assert width >= min_width,  _less_than(width, "width", min_width)
    assert height >= min_height, _less_than(height, "height", min_height)

    # Create the root Tk object.
    root = Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = Frame()
    frame.master.title(title)
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call canvas.update to update the stored width and height
    # with the actual width and height after packing.
    canvas.update()

    _started = True
    return canvas


def draw_line(canvas, x0, y0, x1, y1, *args, width=1, fill="black"):
    """Draw a that line goes through the series of points
        (x0, y0), (x1, y1), ... (xn, yn)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the line's width; default is 1 pixel
        fill: the line's color; default is black
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_line"
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    for i in range(len(args)):
        assert isinstance(args[i], Number), "each coordinate must be a number"
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(fill, str), _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    args = list(args)
    for i in range(1, len(args), 2):
        args[i] = height - args[i]
    canvas.create_line(x0, height-y0, x1, height-y1, *args,
            width=width, fill=fill)


def draw_oval(canvas, x0, y0, x1, y1, *,
        width=1, outline="black", fill=""):
    """Draw an oval (ellipse) inside the bounding box defined by the
        coordinates (x0, y0), (x1, y1)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the width of the oval's outline; default is 1 pixel
        outline: the color of the oval's outline; default is black
        fill: the color of the oval's interior; default is "" which
            means transparent
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_oval"
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_oval(x0, height-y0, x1, height-y1,
            width=width, outline=outline, fill=fill)


def draw_arc(canvas, x0, y0, x1, y1, *,
        start=0, extent=90, width=1, outline="black", fill=""):
    """Draw a wedge shaped slice taken from an oval (ellipse) defined by
        the bounding box coordinates (x0, y0), (x1, y1).

    Parameters
        canvas: the canvas returned from the start_drawing function
        start: starting angle for the slice, in degrees, measured
            counterclockwise from the positive x axis; default is
            0 degrees.
        extent: width of the slice in degrees; default is 90 degrees.
            The slice starts at the angle given by the start parameter
            and extends counterclockwise for extent degrees.
        width: the width of the oval's outline; default is 1 pixel
        outline: the color of the oval's outline; default is black
        fill: the color of the oval's interior; default is "" which
            means transparent
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_arc"
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(start, Number),  _wrong_type(start, "start", "number")
    assert isinstance(extent, Number), _wrong_type(extent, "extent", "number")
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_arc(x0, height-y0, x1, height-y1,
            start=start, extent=extent,
            width=width, outline=outline, fill=fill)


def draw_rectangle(canvas, x0, y0, x1, y1, *,
        width=1, outline="black", fill=""):
    """Draw a rectangle with two corners at (x0, y0), (x1, y1)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the width of the rectangle's outline; default is 1 pixel
        outline: the color of the rectangle's outline; default is black
        fill: the color of the rectangle's interior; default is "" which
            means transparent
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_rectangle"
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_rectangle(x0, height-y0, x1, height-y1,
            width=width, outline=outline, fill=fill)


def draw_polygon(canvas, x0, y0, x1, y1, x2, y2, *args,
        width=1, outline="black", fill=""):
    """Draw a polygon with vertices (x0, y0), (x1, y1), ... (xn, yn).
    The polygon is always a closed polygon the same quantity of segments
    as vertices. In other words, the segments are defined as follows:
    (x0, y0) -> (x1, y1) -> ... -> (xn, yn) -> (x0, y0)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the width of the polygon's outline; default is 1 pixel
        outline: the color of the polygon's outline; default is black
        fill: the color of the polygon's interior; default is "" which
            means transparent
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_polygon"
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(x2, Number), _wrong_type(x2, "x2", "number")
    assert isinstance(y2, Number), _wrong_type(y2, "y2", "number")
    for i in range(len(args)):
        assert isinstance(args[i], Number), "each coordinate must be a number"
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    args = list(args)
    for i in range(1, len(args), 2):
        args[i] = height - args[i]
    canvas.create_polygon(x0, height-y0, x1, height-y1, x2, height-y2,
            *args, width=width, outline=outline, fill=fill)


def draw_text(canvas, center_x, center_y, text, *, fill="black"):
    """Draw text with the center of the text at (center_x, center_y).

    Parameters
        canvas: the canvas returned from the start_drawing function
        text: the text to be drawn. To force a line break, include a
            newline character ("\n").
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_text"
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(center_x, Number), \
        _wrong_type(center_x, "center_x", "number")
    assert isinstance(center_y, Number), \
        _wrong_type(center_y, "center_y", "number")
    assert isinstance(text, str), _wrong_type(text, "text", "string")
    assert isinstance(fill, str), _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_text(center_x, height-center_y, text=text, fill=fill)


def finish_drawing(canvas):
    """Call all functions that are necessary to display
    the drawing on the computer's monitor.

    Parameters
        canvas: the canvas returned from the start_drawing function
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls finish_drawing"
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    canvas.mainloop()


def _wrong_type(param, name, expected):
    # Of course, it's possible to rewrite this function so that it
    # includes an assertion statement which would make less code in this
    # file. Unfortunately, placing the assert in this function adds
    # another level to the stack trace that is printed when the computer
    # raises an AssertionError. It's best not to have the additional
    # level in the stack trace because the error messages in this file
    # are for students.
    return f"wrong data type for parameter {name};" \
        f" {name} is a {type(param)} but must be a {expected}"


def _wrong_type_2(param, name, expected, minimum):
    return _wrong_type(param, name, expected) + \
        f" greater than or equal to {minimum}"


def _less_than(param, name, minimum):
    return f"parameter {name} is {param}" \
        " but must be greater than or equal to {minimum}"


if __name__ == "__main__":
    assert False, \
    f"{__file__} is not a program. It is a library of functions that" \
    " draw 2-dimensional shapes to a canvs in a computer window. You" \
    " are not supposed to run this file but instead import its" \
    " functions into your program and run your program."
