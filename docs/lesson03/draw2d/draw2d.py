# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
This is a library of drawing functions used by BYU-Idaho CSE 111
students to complete an assignment that draws an outdoor scene to a
window. The intent of the assignment is to teach students to separate
a large program into functions with parameters.

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

from tkinter import Tk, Frame, Canvas, BOTH, ARC
from numbers import Number
import math

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
    assert isinstance(title, str), _wrong_type("title", title, "string")
    for name, dimen, min_dimen in \
            (("width", width, 100), ("height", height, 100)):
        assert isinstance(dimen, Number), \
            _wrong_type_2(name, dimen, "number", min_dimen)
        assert dimen >= min_dimen, _less_than(name, dimen, min_dimen)

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


def draw_line(canvas, x0, y0, x1, y1, *coords, width=1, fill="black"):
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
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("x0", x0), ("y0", y0), ("x1", x1), ("y1", y1)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    for coord in coords:
        assert isinstance(coord, Number), "each coordinate must be a number"
    assert isinstance(width, Number), _wrong_type_2("width", width, "number", 0)
    assert width >= 0, _less_than("width", width, 0)
    assert isinstance(fill, str), _wrong_type("fill", fill, "string")

    height = canvas.winfo_height()
    coords = list(coords)
    for i in range(1, len(coords), 2):
        coords[i] = height - coords[i]
    canvas.create_line(x0, height-y0, x1, height-y1, *coords,
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
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("x0", x0), ("y0", y0), ("x1", x1), ("y1", y1)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    assert isinstance(width, Number), _wrong_type_2("width", width, "number", 0)
    assert width >= 0, _less_than("width", width, 0)
    for name, param in (("outline", outline), ("fill", fill)):
        assert isinstance(param, str), _wrong_type(name, param, "string")

    height = canvas.winfo_height()
    canvas.create_oval(x0, height-y0, x1, height-y1,
            width=width, outline=outline, fill=fill)


def draw_arc(canvas, x0, y0, x1, y1, *,
        start=0, extent=90, width=1, outline="black", fill=""):
    """Draw a wedge shaped slice taken from an oval (ellipse) defined
    by the bounding box coordinates (x0, y0), (x1, y1).

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
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("x0", x0), ("y0", y0), ("x1", x1), ("y1", y1),
                        ("start", start), ("extent", extent)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    assert isinstance(width, Number), _wrong_type_2("width", width, "number", 0)
    assert width >= 0, _less_than("width", width, 0)
    for name, param in (("outline", outline), ("fill", fill)):
        assert isinstance(param, str), _wrong_type(name, param, "string")

    height = canvas.winfo_height()
    canvas.create_arc(x0, height-y0, x1, height-y1,
            start=start, extent=extent,
            width=width, outline=outline, fill=fill, style=ARC)


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
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("x0", x0), ("y0", y0), ("x1", x1), ("y1", y1)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    assert isinstance(width, Number), _wrong_type_2("width", width, "number", 0)
    assert width >= 0, _less_than("width", width, 0)
    for name, param in (("outline", outline), ("fill", fill)):
        assert isinstance(param, str), _wrong_type(name, param, "string")

    height = canvas.winfo_height()
    canvas.create_rectangle(x0, height-y0, x1, height-y1,
            width=width, outline=outline, fill=fill)


def draw_vertical_gradient(canvas, x0, y0, color0, x1, y1, color1):
    """Draw a rectangle with a vertical gradient from color0 to color1.
    The two corners of the rectangle will be at (x0, y0), (x1, y1).
    y0 must be less than y1.

    Parameters
        canvas: the canvas returned from the start_drawing function
        color0: a list containing three integers for the red, green,
            and blue of the first color. Each integer must be between
            0 and 255 inclusive.
        color1: a list containing three integers for the red, green,
            and blue of the second color. Each integer must be between
            0 and 255 inclusive.
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_vertical_gradient"
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("x0", x0), ("y0", y0), ("x1", x1), ("y1", y1)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    assert y0 < y1, "y0 must be less than y1"
    for name, color in (("color0", color0), ("color1", color1)):
        assert isinstance(color, list) or isinstance(color, tuple), \
            _wrong_type(name, color, "list or tuple")
        assert len(color) == 3, \
            f"{name} must be a list or tuple containing three" \
            " integers between 0 and 255 inclusive"
        for channel in color:
            assert isinstance(channel, int), \
                f"{name} must be a list or tuple containing three" \
                " integers between 0 and 255 inclusive"
            assert 0 <= channel <= 255, \
                f"{name} must be a list or tuple containing three" \
                " integers between 0 and 255 inclusive"
    height = canvas.winfo_height()

    # Separate color0 into its three channels: red, green, and blue.
    r0, g0, b0 = color0

    # Separate color1 into its three channels: red, green, and blue.
    r1, g1, b1 = color1

    # Compute the amount that each color channel
    # will change from one line to the next.
    diff_y = y1 - y0 + 1
    delta_r = (r1 - r0) / diff_y
    delta_g = (g1 - g0) / diff_y
    delta_b = (b1 - b0) / diff_y

    # Draw the gradient, one line at a time.
    for line in range(diff_y):
        y = height - (y0 + line)
        r = r0 + delta_r * line
        g = g0 + delta_g * line
        b = b0 + delta_b * line
        color = _make_color(r, g, b)
        canvas.create_line(x0, y, x1, y, width=1, fill=color)


def draw_horizontal_gradient(canvas, x0, y0, color0, x1, y1, color1):
    """Draw a rectangle with a horizontal gradient from color0 to color1.
    The two corners of the rectangle will be at (x0, y0), (x1, y1).
    x0 must be less than x1.

    Parameters
        canvas: the canvas returned from the start_drawing function
        color0: a list containing three integers for the red, green,
            and blue of the first color. Each integer must be between
            0 and 255 inclusive.
        color1: a list containing three integers for the red, green,
            and blue of the second color. Each integer must be between
            0 and 255 inclusive.
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_horizontal_gradient"
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("x0", x0), ("y0", y0), ("x1", x1), ("y1", y1)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    assert x0 < x1, "x0 must be less than x1"
    for name, color in (("color0", color0), ("color1", color1)):
        assert isinstance(color, list) or isinstance(color, tuple), \
            _wrong_type(name, color, "list or tuple")
        assert len(color) == 3, \
            f"{name} must be a list or tuple containing three" \
            " integers between 0 and 255 inclusive"
        for channel in color:
            assert isinstance(channel, int), \
                f"{name} must be a list or tuple containing three" \
                " integers between 0 and 255 inclusive"
            assert 0 <= channel <= 255, \
                f"{name} must be a list or tuple containing three" \
                " integers between 0 and 255 inclusive"
    height = canvas.winfo_height()

    # Separate color0 into its three channels: red, green, and blue.
    r0, g0, b0 = color0

    # Separate color1 into its three channels: red, green, and blue.
    r1, g1, b1 = color1

    # Compute the amount that each color channel
    # will change from one line to the next.
    diff_x = x1 - x0 + 1
    delta_r = (r1 - r0) / diff_x
    delta_g = (g1 - g0) / diff_x
    delta_b = (b1 - b0) / diff_x

    y0 = height - y0
    y1 = height - y1

    # Draw the gradient, one line at a time.
    for line in range(diff_x):
        x = x0 + line
        r = r0 + delta_r * line
        g = g0 + delta_g * line
        b = b0 + delta_b * line
        color = _make_color(r, g, b)
        canvas.create_line(x, y0, x, y1, width=1, fill=color)


def draw_circle_with_vert_grad(canvas, center_x, center_y, radius,
        color_center, color_edge):
    """Draw a circle with a vertical gradient from the center to both
    the top and bottom edges. The center of the circle will be at
    (center_x, center_y).

    Parameters
        canvas: the canvas returned from the start_drawing function
        radius: the radius in pixels of the circle
        color_center: a list containing three integers for the red,
            green, and blue of the center of the circle. Each integer
            must be between 0 and 255 inclusive.
        color_edge: a list containing three integers for the red,
            green, and blue of the top and bottom edges of the circle.
            Each integer must be between 0 and 255 inclusive.
    Return: nothing
    """
    assert _started, \
        "your program must call start_drawing before it calls draw_circle_with_vert_grad"
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("center_x", center_x), ("center_y", center_y)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    for name, color in (("color_center", color_center),
            ("color_edge", color_edge)):
        assert isinstance(color, list) or isinstance(color, tuple), \
            _wrong_type(name, color, "list or tuple")
        assert len(color) == 3, \
            f"{name} must be a list or tuple containing three" \
            " integers between 0 and 255 inclusive"
        for channel in color:
            assert isinstance(channel, int), \
                f"{name} must be a list or tuple containing three" \
                " integers between 0 and 255 inclusive"
            assert 0 <= channel <= 255, \
                f"{name} must be a list or tuple containing three" \
                " integers between 0 and 255 inclusive"
    height = canvas.winfo_height()

    # Separate color_center into its three channels: red, green, and blue.
    rc, gc, bc = color_center

    # Separate color_edge into its three channels: red, green, and blue.
    re, ge, be = color_edge

    diff_y = 2 * radius
    delta_r = (re - rc) / diff_y
    delta_g = (ge - gc) / diff_y
    delta_b = (be - bc) / diff_y

    for line in range(radius):
        r = rc + delta_r * line
        g = gc + delta_g * line
        b = bc + delta_b * line
        color = _make_color(r, g, b)
        x = math.sqrt(radius**2 - line**2)
        x0 = center_x - x
        x1 = center_x + x
        y0 = height - (center_y - line)
        canvas.create_line(x0, y0, x1, y0, width=1, fill=color)
        y1 = height - (center_y + line)
        canvas.create_line(x0, y1, x1, y1, width=1, fill=color)


def draw_polygon(canvas, x0, y0, x1, y1, x2, y2, *coords,
        width=1, outline="black", fill=""):
    """Draw a polygon with vertices at (x0, y0), (x1, y1), ... (xn, yn).
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
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("x0", x0), ("y0", y0), ("x1", x1), ("y1", y1),
                        ("x2", x2), ("y2", y2)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    for coord in coords:
        assert isinstance(coord, Number), "each coordinate must be a number"
    assert isinstance(width, Number), _wrong_type_2("width", width, "number", 0)
    assert width >= 0, _less_than("width", width, 0)
    for name, param in (("outline", outline), ("fill", fill)):
        assert isinstance(param, str), _wrong_type(name, param, "string")

    height = canvas.winfo_height()
    coords = list(coords)
    for i in range(1, len(coords), 2):
        coords[i] = height - coords[i]
    canvas.create_polygon(x0, height-y0, x1, height-y1, x2, height-y2,
            *coords, width=width, outline=outline, fill=fill)


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
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")
    for name, coord in (("center_x", center_x), ("center_y", center_y)):
        assert isinstance(coord, Number), _wrong_type(name, coord, "number")
    for name, param in (("text", text), ("fill", fill)):
        assert isinstance(param, str), _wrong_type(name, param, "string")

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
    assert isinstance(canvas, Canvas), _wrong_type("canvas", canvas, "Canvas")

    canvas.mainloop()


def _make_color(r, g, b):
    """Convert red, green, and blue into a color
    in the hexadecimal form "#rrggbb"
    """
    return "#" + _hex_str(r) + _hex_str(g) + _hex_str(b)


def _hex_str(n):
    n = int(round(n, 0))
    assert 0 <= n <= 255
    s = hex(n)[2:]
    if len(s) == 1:
        s = "0" + s
    return s


def _wrong_type(name, param, expected):
    # Of course, it's possible to rewrite this function so that it
    # includes an assertion statement which would make less code in
    # this file. Unfortunately, placing the assert in this function
    # adds another level to the stack trace that is printed when the
    # computer raises an AssertionError. It's best not to have the
    # additional level in the stack trace because the error messages
    # in this file are for students.
    return f"wrong data type for parameter {name};" \
        f" {name} is a {type(param)} but must be a {expected}"


def _wrong_type_2(name, param, expected, minimum):
    return _wrong_type(name, param, expected) + \
        f" greater than or equal to {minimum}"


def _less_than(name, param, minimum):
    return f"parameter {name} is {param} but" \
        " must be greater than or equal to {minimum}"


if __name__ == "__main__":
    assert False, \
    f"{__file__} is not a program. It is a library of functions" \
    " that draw 2-dimensional shapes to a canvas in a computer" \
    " window. You are not supposed to run this file but instead" \
    " import its functions into your program and run your program."
