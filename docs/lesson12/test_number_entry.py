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
    frm_main.master.title("Test Number Entries")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    ranges = [
        ((-50, -1), (-50, -1)),
        (None,      (-50, -0.8)),
        ((-50, 0),  (-50, 0)),
        (None,      (-50, 0.8)),
        ((-50, 1),  (-50, 1)),
        ((-50, 50), (-50, 50)),
        (None,      (-1, -0.8)),
        ((-1, 0),   (-1, 0)),
        (None,      (-1, 0.8)),
        ((-1, 1),   (-1, 1)),
        ((-1, 50),  (-1, 50)),
        (None,      (-0.8, 0)),
        (None,      (-0.8, 0.8)),
        (None,      (-0.8, 1)),
        (None,      (-0.8, 50)),
        (None,      (0, 0.8)),
        ((0, 1),    (0, 1)),
        ((0, 50),   (0, 50)),
        (None,      (0.8, 1)),
        (None,      (0.8, 50)),
        ((1, 50),   (1, 50))
    ]
    entries = []

    row = 0
    lbl_int = Label(frm_main, text="integer:")
    ent_int = IntEntry(frm_main, width=4)
    lbl_int.grid(row=row, column=0, padx=3, pady=2, sticky="e")
    ent_int.grid(row=row, column=1, padx=3, pady=2, sticky="w")
    entries.append(ent_int)
    lbl_float = Label(frm_main, text="float:")
    ent_float = FloatEntry(frm_main, width=4)
    lbl_float.grid(row=row, column=2, padx=3, pady=2, sticky="e")
    ent_float.grid(row=row, column=3, padx=3, pady=2, sticky="w")
    entries.append(ent_float)
    row += 1

    # Create labels and number entries.
    for int_range, float_range in ranges:
        if int_range is not None:
            int_lower, int_upper = int_range
            lbl_int = Label(frm_main,
                    text=f"integer [{int_lower}, {int_upper}]:")
            ent_int = IntEntry(frm_main, width=4,
                    lower_bound=int_lower, upper_bound=int_upper)
            lbl_int.grid(row=row, column=0, padx=3, pady=2, sticky="e")
            ent_int.grid(row=row, column=1, padx=3, pady=2, sticky="w")
            entries.append(ent_int)

        float_lower, float_upper = float_range
        lbl_float = Label(frm_main,
                text=f"float [{float_lower}, {float_upper}]:")
        ent_float = FloatEntry(frm_main, width=4,
                lower_bound=float_lower, upper_bound=float_upper)
        lbl_float.grid(row=row, column=2, padx=3, pady=2, sticky="e")
        ent_float.grid(row=row, column=3, padx=3, pady=2, sticky="w")
        entries.append(ent_float)

        row += 1

    # Create a label to display the result.
    lbl_correct = Label(frm_main, text="All correct:")
    txt_correct = Label(frm_main)
    lbl_correct.grid(row=row, column=0, padx=3, pady=2, sticky="e")
    txt_correct.grid(row=row, column=1, columnspan=2, padx=3, pady=2, sticky="w")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")
    btn_clear.grid(row=row, column=3, padx=3, pady=2, sticky="e")

    # This function is called each time the user releases a key.
    def check_all(event):
        """Compute the approximate volume of a tire in liters."""
        i = 0
        entry = None
        try:
            for i, entry in enumerate(entries):
                value = entry.get()
            txt_correct.config(text="Yes!")
        except ValueError:
            # When the user deletes all the digits in one
            # of the number entries, clear the result.
            txt_correct.config(text=f"Incorrect at index {i}")


    # This function is called each time
    # the user clicks the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        for entry in entries:
            entry.clear()
        txt_correct.config(text="")
        entries[0].focus()


    # Bind the calculate function to the three number
    # entries so that the calculate function will be called
    # when the user changes the text in the number entries.
    for entry in entries:
        entry.bind("<KeyRelease>", check_all)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width text field.
    entries[0].focus()


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
