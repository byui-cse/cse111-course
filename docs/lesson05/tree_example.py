from tkinter import Tk, Frame, Canvas, BOTH

def main():
    width = 800
    height = 600

    # Create the root Tk object.
    root = Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = Frame()
    frame.master.title("Scene")
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):

    # Call the draw_pine_tree function to draw a tree.
    tree_left = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_pine_tree(canvas, tree_left, tree_top, tree_height)


# Define a function that draws a pine tree
def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree."""
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

main()