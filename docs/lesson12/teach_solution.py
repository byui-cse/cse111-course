# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import math
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Tire Volume")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create labels for the number entries and the result.
    lbl_width = Label(frm_main, text="Width (80 - 300):")
    lbl_ratio = Label(frm_main, text="Aspect Ratio (30 - 90):")
    lbl_diam = Label(frm_main, text="Diameter (7 - 30):")
    lbl_volume = Label(frm_main, text="Volume:")

    # Create three number entries.
    ent_width = IntEntry(frm_main, width=5, lower_bound=80, upper_bound=300)
    ent_ratio = IntEntry(frm_main, width=5, lower_bound=30, upper_bound=90)
    ent_diam = FloatEntry(frm_main, width=5, lower_bound=7, upper_bound=30)

    # Create a label to display the result.
    txt_volume = Label(frm_main, width=5, anchor="e")

    # Create labels to display the units.
    lbl_width_units = Label(frm_main, text="millimeters")
    # Ratios don't have units
    lbl_diam_units = Label(frm_main, text="inches")
    lbl_vol_units = Label(frm_main, text="liters")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, number entries, and buttons in a grid.
    lbl_width.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
    ent_width.grid(      row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_width_units.grid(row=0, column=2, padx=0, pady=2, sticky="w")

    lbl_ratio.grid(     row=1, column=0, padx=3, pady=2, sticky="e")
    ent_ratio.grid(     row=1, column=1, padx=3, pady=2, sticky="w")
    # Ratios don't have units.

    lbl_diam.grid(      row=2, column=0, padx=3, pady=2, sticky="e")
    ent_diam.grid(      row=2, column=1, padx=3, pady=2, sticky="w")
    lbl_diam_units.grid(row=2, column=2, padx=0, pady=2, sticky="w")

    lbl_volume.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
    txt_volume.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
    lbl_vol_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
    btn_clear.grid(    row=3, column=3, padx=3, pady=2)


    # This function is called each time the user releases a key.
    def calculate(event):
        """Compute the approximate volume of a tire in liters."""
        try:
            # Get the user input.
            w = ent_width.get()
            a = ent_ratio.get()
            d = ent_diam.get()

            # Compute the tire volume in liters.
            v = (math.pi * w * w * a * (w * a + 2540 * d)) / 10_000_000_000

            # Display the volume rounded to one digit
            # after the decimal for the user to see.
            txt_volume.config(text=f"{v:.2f}")

        except ValueError:
            # When the user deletes all the digits in one
            # of the number entries, clear the result.
            txt_volume.config(text="")


    # This function is called each time
    # the user clicks the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_width.clear()
        ent_ratio.clear()
        ent_diam.clear()
        txt_volume.config(text="")
        ent_width.focus()


    # Bind the calculate function to the three number
    # entries so that the calculate function will be called
    # when the user changes the text in the number entries.
    ent_width.bind("<KeyRelease>", calculate)
    ent_ratio.bind("<KeyRelease>", calculate)
    ent_diam.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width text field.
    ent_width.focus()


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
