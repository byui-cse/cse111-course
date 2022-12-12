# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""This module contains two classes, IntEntry and FloatEntry, that allow
a user to enter an integer or a floating point number into a tkinter
Entry widget.
"""
import tkinter as tk
from tkinter import Entry
from numbers import Number
from sys import float_info

"""
Can this user input become a number within the range [lower, upper]

All possibilities
[ < 0, < 0 ]    require -
[ < 0, 0 ]      allow -
[ < 0, > 0 ]    allow -
[ 0, > 0 ]      disallow -
[ > 0, > 0 ]    disallow -
"""

class IntEntry(Entry):
    """An Entry widget that accepts only integers between
    an optional lower bound and an optional upper bound.
    """
    def __init__(self, parent, *,
            lower_bound=-2**63, upper_bound=2**63 - 1, **kwargs):
        super().__init__(parent)
        assert isinstance(lower_bound, int), "lower_bound must be an int"
        assert isinstance(upper_bound, int), "upper_bound must be an int"
        assert lower_bound < upper_bound, \
            "lower_bound must be less than upper_bound"

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.lower_entry = lower_bound if lower_bound <= 1 else 1
        self.upper_entry = upper_bound if upper_bound >= -1 else -1
        if "justify" not in kwargs:
            kwargs["justify"] = "right"
        if "width" not in kwargs:
            kwargs["width"] = max(len(str(lower_bound)), len(str(upper_bound)))
        kwargs["validate"] = "key"
        kwargs["validatecommand"] = (parent.register(self.validate), "%P")
        self.config(**kwargs)
        self.bind("<FocusIn>", select_all)


    def validate(self, value_if_allowed):
        valid = False
        try:
            i = int(value_if_allowed)
            valid = (str(i) == value_if_allowed and
                    self.lower_entry <= i <= self.upper_entry)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower_entry < 0 and value_if_allowed == "-"))
        return valid


    def get(self):
        """Return the integer that the user entered."""
        value = int(super().get())
        if value < self.lower_bound or self.upper_bound < value:
            raise ValueError("number must be between"
                f" {self.lower_bound} and {self.upper_bound}")
        return value


    def set(self, n):
        """Display an integer for the user to see."""
        assert isinstance(n, int), "n must be an integer"
        assert self.lower_bound <= n <= self.upper_bound, \
            f"n must be between {self.lower_bound} and {self.upper_bound}"
        self.delete(0, tk.END)
        self.insert(0, str(n))


class FloatEntry(tk.Entry):
    """An Entry widget that accepts only numbers between
    an optional lower bound and an optional upper bound.
    """
    def __init__(self, parent, *, lower_bound=-float_info.max,
            upper_bound=float_info.max, **kwargs):
        super().__init__(parent)
        assert isinstance(lower_bound, Number), "lower_bound must be a number"
        assert isinstance(upper_bound, Number), "upper_bound must be a number"
        assert lower_bound < upper_bound, \
            "lower_bound must be less than upper_bound"

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.lower_entry = lower_bound if lower_bound <= 0 else 0
        self.upper_entry = upper_bound if upper_bound >= 0 else 0
        if not "justify" in kwargs:
            kwargs["justify"] = "right"
        if not "width" in kwargs:
            kwargs["width"] = max(len(str(lower_bound)), len(str(upper_bound)))
        kwargs["validate"] = "key"
        kwargs["validatecommand"] = (parent.register(self.validate), "%P")
        self.config(**kwargs)
        self.bind("<FocusIn>", select_all)


    def validate(self, value_if_allowed):
        valid = False
        try:
            f = float(value_if_allowed)
            valid = (self.lower_entry <= f <= self.upper_entry)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower_entry < 0 and value_if_allowed == "-"))
        return valid


    def get(self):
        """Return the number that the user entered."""
        return float(super().get())
        if value < self.lower_bound or self.upper_bound < value:
            raise ValueError("number must be between"
                f" {self.lower_bound} and {self.upper_bound}")
        return value


    def set(self, n):
        """Display a number for the user to see."""
        assert isinstance(n, Number), "n must be an integer"
        assert self.lower_bound <= n <= self.upper_bound, \
            f"n must be between {self.lower_bound} and {self.upper_bound}"
        self.delete(0, tk.END)
        self.insert(0, str(n))


def select_all(event):
    entry = event.widget;
    entry.select_range(0, tk.END)
    entry.icursor(tk.END)
