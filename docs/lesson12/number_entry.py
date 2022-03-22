# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""This module contains two classes, IntEntry and FloatEntry,
that allow a user to enter an integer or a floating point number.
"""
import tkinter as tk
from numbers import Number


class IntEntry(tk.Entry):
    """An Entry widget that accepts only
    integers between a lower and upper bound.
    """
    def __init__(self, parent, lower_bound, upper_bound, **kwargs):
        super().__init__(parent)
        if lower_bound > 1:
            lower_bound = 1
        if upper_bound < -1:
            upper_bound = -1
        assert isinstance(lower_bound, int), "lower_bound must be an int"
        assert isinstance(upper_bound, int), "upper_bound must be an int"
        assert lower_bound <= upper_bound, \
            "lower_bound must be less than upper_bound"

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        if "justify" not in kwargs:
            kwargs["justify"] = "right"
        if "width" not in kwargs:
            kwargs["width"] = max(len(str(lower_bound)), len(str(upper_bound)))
        kwargs["validate"] = "key"
        kwargs["validatecommand"] = (parent.register(self.validate), "%P")
        self.config(**kwargs)


    def validate(self, value_if_allowed):
        valid = False
        try:
            i = int(value_if_allowed)
            valid = (str(i) == value_if_allowed and
                    self.lower_bound <= i and i <= self.upper_bound)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower_bound < 0 and value_if_allowed == "-"))
        return valid


    def get(self):
        """Return the integer that the user entered."""
        return int(super().get())


    def set(self, n):
        """Display the integer n for the user to see."""
        self.delete(0, tk.END)
        self.insert(0, str(int(n)))


class FloatEntry(tk.Entry):
    """An Entry widget that accepts only
    numbers between a lower and upper bound.
    """
    def __init__(self, parent, lower_bound, upper_bound, **kwargs):
        super().__init__(parent)
        if lower_bound > 0:
            lower_bound = 0
        if upper_bound < 0:
            upper_bound = 0
        assert isinstance(lower_bound, Number), "lower_bound must be a number"
        assert isinstance(upper_bound, Number), "upper_bound must be a number"
        assert lower_bound <= upper_bound, \
            "lower_bound must be less than upper_bound"

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        vcmd = (parent.register(self.validate), "%P")
        if not "justify" in kwargs:
            kwargs["justify"] = "right"
        if not "width" in kwargs:
            kwargs["width"] = max(len(str(lower_bound)), len(str(upper_bound)))
        self.config(validate="key", validatecommand=vcmd, **kwargs)


    def validate(self, value_if_allowed):
        valid = False
        try:
            i = float(value_if_allowed)
            valid = (self.lower_bound <= i and i <= self.upper_bound)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower_bound < 0 and value_if_allowed == "-"))
        return valid


    def get(self):
        """Return the number that the user entered."""
        return float(super().get())


    def set(self, n):
        """Display the number n for the user to see."""
        self.delete(0, tk.END)
        self.insert(0, str(float(n)))
