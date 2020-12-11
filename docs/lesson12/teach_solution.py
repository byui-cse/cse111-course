import math
import tkinter as tk
from number_entry import IntEntry, FloatEntry


def main():
    try:
        # Create the root Tk object.
        app = tk.Tk()

        # Create a TireWindow object which will call
        # the __init__ function in the TireWindow class.
        TireWindow(app)

        # Start the tkinter loop that processes user events
        # such as key presses and mouse button clicks.
        app.mainloop()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


class TireWindow(tk.Frame):
    """The main window of this application."""

    def __init__(self, parent):
        """Initialize a Frame object."""

        # Call __init__ in the parent class.
        super().__init__(parent)

        # Create labels for the text fields and the results.
        lblWidth = tk.Label(self, text="Width (mm):")
        lblRatio = tk.Label(self, text="Aspect Ratio:")
        lblDiam = tk.Label(self, text="Diameter (in):")
        lblVol = tk.Label(self, text="Volume (cubic cm):")

        # Create three text fields.
        txtWidth = IntEntry(self, 1, 300, width=5)
        txtRatio = FloatEntry(self, 1, 90, width=5)
        txtDiam = FloatEntry(self, 1, 30, width=5)

        # Create a label to display the result.
        lblResult = tk.Label(self, width=8, anchor="w")

        # Create the Clear button.
        btnClear = tk.Button(self, text="Clear")

        # Layout all the labels, text fields, and buttons in a grid.
        lblWidth.grid( row=0, column=0, padx=3, pady=2, sticky="e")
        txtWidth.grid( row=0, column=1, padx=3, pady=2, sticky="w")
        lblRatio.grid( row=1, column=0, padx=3, pady=2, sticky="e")
        txtRatio.grid( row=1, column=1, padx=3, pady=2, sticky="w")
        lblDiam.grid(  row=2, column=0, padx=3, pady=2, sticky="e")
        txtDiam.grid(  row=2, column=1, padx=3, pady=2, sticky="w")
        lblVol.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
        lblResult.grid(row=3, column=1, padx=3, pady=2, sticky="w")
        btnClear.grid( row=3, column=2, padx=3, pady=2)

        self.master.title("Tire Volume")
        self.grid(padx=3, pady=3)


        # This function is called each time the user releases a key.
        def calc(event):
            """Compute the approximate volume of a tire in cubic cm."""
            try:
                # Get the user input.
                w = txtWidth.get()
                a = txtRatio.get()
                d = txtDiam.get()

                # Compute the tire volume.
                v = (math.pi * w * w * a * (w * a + 2540 * d)) / 10_000_000

                # Display the volume for the user to see.
                lblResult.config(text=str(round(v, 1)))

            except ValueError:
                # When the user deletes all the digits in one
                # of the text fields, clear the result labels.
                lblResult.config(text="")


        # This function is called each time
        # the user clicks the "Clear" button.
        def clear():
            """Clear all the inputs and outputs."""
            txtWidth.delete(0, tk.END)
            txtRatio.delete(0, tk.END)
            txtDiam.delete(0, tk.END)
            lblResult.config(text="")
            txtWidth.focus()


        # Bind the calc function to the three text fields
        # so that the calc function will be called when the
        # user changes the text in the text fields.
        txtWidth.bind("<KeyRelease>", calc)
        txtRatio.bind("<KeyRelease>", calc)
        txtDiam.bind("<KeyRelease>", calc)

        # Bind the clear function to the clear button so
        # that the clear function will be called when the
        # user clicks the clear button.
        btnClear.config(command=clear)

        # Give the keyboard focus to the width text field.
        txtWidth.focus()


# If this file was executed like this:
# python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
