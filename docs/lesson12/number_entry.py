import tkinter as tk


class IntEntry(tk.Entry):
    """An Entry widget that accepts only
    integers between a lower and upper bound.
    """
    def __init__(self, parent, lower, upper, **kwargs):
        super().__init__(parent)
        if lower > 1:
            lower = 1
        if upper < -1:
            upper = -1
        self.lower = lower
        self.upper = upper
        if "justify" not in kwargs:
            kwargs["justify"] = "right"
        if "width" not in kwargs:
            kwargs["width"] = max(len(str(lower)), len(str(upper)))
        kwargs["validate"] = "key"
        kwargs["validatecommand"] = (parent.register(self.validate), "%P")
        self.config(**kwargs)

    def validate(self, value_if_allowed):
        valid = False
        try:
            i = int(value_if_allowed)
            valid = (str(i) == value_if_allowed and
                    self.lower <= i and i <= self.upper)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower < 0 and value_if_allowed == "-"))
        return valid

    def get(self):
        """Return the integer that the user entered."""
        return int(super().get())

    def set(self, n):
        """Display the integer n for the user to see."""
        self.delete(0, tk.END)
        self.insert(0, str(int(n)))

    def clear(self):
        """Clear the integer, if any, that is in this IntEntry."""
        self.delete(0, tk.END)


class FloatEntry(tk.Entry):
    """An Entry widget that accepts only
    numbers between a lower and upper bound.
    """
    def __init__(self, parent, lower, upper, **kwargs):
        super().__init__(parent)
        if lower > 0:
            lower = 0
        if upper < 0:
            upper = 0
        self.lower = lower
        self.upper = upper
        vcmd = (parent.register(self.validate), "%P")
        if not "justify" in kwargs:
            kwargs["justify"] = "right"
        if not "width" in kwargs:
            kwargs["width"] = max(len(str(lower)), len(str(upper)))
        self.config(validate="key", validatecommand=vcmd, **kwargs)

    def validate(self, value_if_allowed):
        valid = False
        try:
            i = float(value_if_allowed)
            valid = (self.lower <= i and i <= self.upper)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower < 0 and value_if_allowed == "-"))
        return valid

    def get(self):
        """Return the number that the user entered."""
        return float(super().get())

    def set(self, n):
        """Display the number n for the user to see."""
        self.delete(0, tk.END)
        self.insert(0, str(float(n)))

    def clear(self):
        """Clear the number, if any, that is in this FloatEntry."""
        self.delete(0, tk.END)
