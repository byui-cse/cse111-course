from meter_usage import get_int, insert_after
from io import StringIO
import pandas as pd
import pytest
import sys


def test_get_int(monkeypatch):
    """Verify that the get_int function does not return a value
    until the user input is between the minimum and maximum values.
    """
    # Setup simulated user input: hi, -8, 10, and 2
    test_input = StringIO("hi\n-8\n10\n2\n")
    monkeypatch.setattr(sys, "stdin", test_input)

    assert get_int("Please enter an integer: ", -5, 5) == 2


def test_insert_after():
    """Verify that the insert after function
    correctly inserts elements into a list.
    """
    test_cases = [
        ([], "b", "a", ["a"]),
        (["a"], "a", "b", ["a", "b"]),
        (["a"], "b", "c", ["a", "c"]),
        (["a", "c"], "a", "b", ["a", "b", "c"]),
        (["a", "b"], "b", "d", ["a", "b", "d"]),
        (["a", "b"], "c", "e", ["a", "b", "e"])
    ]
    for test_case in test_cases:
        alist = test_case[0]
        existing = test_case[1]
        toinsert = test_case[2]
        result = test_case[3]
        assert insert_after(alist, existing, toinsert) == None
        assert alist == result


pytest.main(["test_meter_usage.py"])
