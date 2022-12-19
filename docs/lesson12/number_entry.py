# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""This module contains two classes, IntEntry and FloatEntry, that allow
a user to enter an integer or a floating-point number into a tkinter
Entry widget.
"""
import tkinter as tk
from tkinter import Entry
from numbers import Number
from sys import float_info


class _NumberEntry(Entry):
    _ERROR_STYLE = {"bg":"pink", "fg":"black"}


    def __init__(self, parent, datatype, dataname,
            lower_bound, upper_bound, default, kwargs):
        super().__init__(parent)

        assert type(self) != _NumberEntry, \
            "can't create a _NumberEntry object; " \
            "only children classes of _NumberEntry can be instantiated"
        assert isinstance(lower_bound, datatype), \
            f"lower_bound must be " + dataname
        assert isinstance(upper_bound, datatype), \
            f"upper_bound must be " + dataname
        assert lower_bound < upper_bound, \
            "lower_bound must be less than upper_bound"

        self.__datatype = datatype
        self.__dataname = dataname
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound

        if default is not None:
            assert isinstance(default, datatype), \
                f"default must be " + dataname
            assert self._in_bounds(default), \
                "default must be between lower_bound and upper_bound"
            self.delete(0, tk.END)
            self.insert(0, str(default))

        self.__set_tk_args(kwargs)
        self.bind("<FocusIn>", _NumberEntry.__select_all)


    def __set_tk_args(self, kwargs):
        """Set the arguments that are used by tkinter."""
        if "justify" not in kwargs:
            kwargs["justify"] = "right"
        if "width" not in kwargs:
            kwargs["width"] = \
                max(len(str(self.__lower_bound)), len(str(self.__upper_bound)))
        kwargs["validate"] = "focusin"
        kwargs["validatecommand"] = \
                (self.register(self.__validate_all), "%V", "%s", "%P")
        self.config(**kwargs)
        self._original_style = {"bg":self["bg"], "fg":self["fg"]}


    # Each time a _NumberEntry gets the keyboard focus,
    # select all the text in that entry.
    @staticmethod
    def __select_all(event):
        """Select all the characters in the entry."""
        entry = event.widget
        entry.select_range(0, tk.END)
        entry.icursor(tk.END)


    @staticmethod
    def _contains_space(text):
        has_space = False
        for ch in text:
            has_space = ch.isspace()
            if has_space:
                break
        return has_space


    def __validate_all(self, reason, current_text, text_if_allowed):
        valid = False
        if reason == "key":
            valid = self._validate_key(current_text, text_if_allowed)
        elif reason == "focusin":
            valid = self.__focus_in(current_text)
        elif reason == "focusout":
            valid = self.__focus_out(current_text)
        return valid


    def __focus_in(self, current_text):
        self.config({"validate": "all"})
        return self.__validate_focus(current_text)

    def __focus_out(self, current_text):
        self.config({"validate": "focusin"})
        return self.__validate_focus(current_text)

    def __validate_focus(self, current_text):
        valid = False
        try:
            n = self._convert(current_text)
            valid = self._in_bounds(n)
        except ValueError:
            pass
        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return valid


    def _in_bounds(self, n):
        return self.__lower_bound <= n <= self.__upper_bound


    def set(self, n):
        """Display a number for the user to see."""
        assert isinstance(n, self.__datatype), \
            "n must be " + self.__dataname
        assert self._in_bounds(n), \
            f"n must be between {self.__lower_bound} and {self.__upper_bound}"
        self.delete(0, tk.END)
        self.insert(0, str(n))


    def get(self):
        """Return the number that the user entered."""
        n = self._convert(super().get())
        if not self._in_bounds(n):
            raise ValueError("number must be between"
                f" {self.__lower_bound} and {self.__upper_bound}")
        return n


    def clear(self):
        self.config({"validate": "focusin"})
        self.config(self._original_style)
        self.delete(0, tk.END)


class IntEntry(_NumberEntry):
    """An Entry widget that accepts only integers between
    an optional lower bound and an optional upper bound.
    """
    def __init__(self, parent, *, lower_bound=-2**63,
            upper_bound=2**63 - 1, default=None, **kwargs):
        super().__init__(parent, int, "an integer",
                lower_bound, upper_bound, default, kwargs)

        self.__lower_entry = lower_bound if lower_bound <= 1 else 1
        self.__upper_entry = upper_bound if upper_bound >= -1 else -1
        self.__allow_negative = (lower_bound < 0)


    def _validate_key(self, current_text, text_if_allowed):
        allowed = valid = False
        try:
            if not _NumberEntry._contains_space(text_if_allowed):
                n = int(text_if_allowed)
                allowed = self.__lower_entry <= n <= self.__upper_entry
                # If text_if_allowed is allowed, we must allow it, and
                # we must check only text_if_allowed for validity.
                if allowed:
                    valid = self._in_bounds(n)
        except ValueError:
            allowed = (len(text_if_allowed) == 0 or
                    (self.__allow_negative and text_if_allowed == "-"))

        # If text_if_allowed is not allowed, we must not allow
        # it, and we must check only current_text for validity.
        if not allowed:
            try:
                n = int(current_text)
                valid = self._in_bounds(n)
            except ValueError:
                pass

        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return allowed


    @staticmethod
    def _convert(text): return int(text)


class FloatEntry(_NumberEntry):
    """An Entry widget that accepts only numbers between
    an optional lower bound and an optional upper bound.
    """
    def __init__(self, parent, *, lower_bound=-float_info.max,
            upper_bound=float_info.max, default=None, **kwargs):
        super().__init__(parent, Number, "a number",
                lower_bound, upper_bound, default, kwargs)

        if lower_bound < 0:    # [-, 0)
            self.__lower_entry = lower_bound
        elif lower_bound < 1:  # [0, 1)
            self.__lower_entry = 0
        else:                  # [1, +]
            self.__lower_entry = 1

        if upper_bound <= -1:   # [-, -1]
            self.__upper_entry = -1
        elif upper_bound <= 0:  # (-1, 0]
            self.__upper_entry = 0
        else:                   # (0, +]
            self.__upper_entry = upper_bound

        self.__allow_negative = (lower_bound < 0)
        self.__allow_leading_dot = (
                (-1 < lower_bound < 1) or
                (-1 < upper_bound < 1) or
                (lower_bound <= -1 and 1 <= upper_bound))


    def _validate_key(self, current_text, text_if_allowed):
        allowed = valid = False
        try:
            if not _NumberEntry._contains_space(text_if_allowed):
                n = float(text_if_allowed)
                allowed = self.__lower_entry <= n <= self.__upper_entry
                # If text_if_allowed is allowed, we must allow it, and
                # we must check only text_if_allowed for validity.
                if allowed:
                    valid = self._in_bounds(n)
        except ValueError:
            allowed = (len(text_if_allowed) == 0 or
                    (self.__allow_negative and text_if_allowed == "-") or
                    (self.__allow_leading_dot and text_if_allowed == ".") or
                    (self.__allow_negative and self.__allow_leading_dot
                        and text_if_allowed == "-."))

        # If text_if_allowed is not allowed, we must not allow
        # it, and we must check only current_text for validity.
        if not allowed:
            try:
                n = float(current_text)
                valid = self._in_bounds(n)
            except ValueError:
                pass

        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return allowed


    @staticmethod
    def _convert(text): return float(text)
