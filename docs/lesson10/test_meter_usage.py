from meter_usage import get_int
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


pytest.main(["-v", "--tb=no", "test_meter_usage.py"])
