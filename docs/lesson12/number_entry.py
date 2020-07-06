import tkinter as tk


class IntEntry(tk.Entry):
    """An Entry widget that accepts only
    integers between an upper and lower bound.
    """
    def __init__(self, parent, lower, upper, **kwargs):
        super().__init__(parent)
        self.lower = lower
        self.upper = upper
        if not "justify" in kwargs:
            kwargs["justify"] = "right"
        if not "width" in kwargs:
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
        return int(super().get())

    def set(self, n):
        self.delete(0, tk.END)
        self.insert(0, str(int(n)))

    def clear(self):
        self.delete(0, tk.END)


class FloatEntry(tk.Entry):
    """An Entry widget that accepts only
    numbers between an upper and lower bound.
    """
    def __init__(self, parent, lower, upper, **kwargs):
        super().__init__(parent)
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
        return float(super().get())

    def set(self, n):
        self.delete(0, tk.END)
        self.insert(0, str(float(n)))

    def clear(self):
        self.delete(0, tk.END)
