# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import math


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library.
    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sun(canvas, 640, 380, 70)
    draw_grid(canvas, scene_width, scene_height, 50)

    finish_drawing(canvas)


def draw_sun(canvas, center_x, center_y, radius):
    color = "gold"

    # Draw the rays extending from the sun.
    length = radius * 2
    interval = 18
    for degrees in range(0, 360, interval):
        radians = math.radians(degrees)
        x = center_x + math.cos(radians) * length
        y = center_y + math.sin(radians) * length
        draw_line(canvas, center_x, center_y, x, y, width=5, fill=color)

    # Draw the ball of the sun.
    left = center_x - radius
    top = center_y + radius
    right = center_x + radius
    bottom = center_y - radius
    draw_oval(canvas, left, top, right, bottom, width=0, fill=color)


def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()
