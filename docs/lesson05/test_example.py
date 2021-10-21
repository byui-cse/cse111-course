# test_example.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

"""Verify that the wind_chill and head_index functions work correctly."""

from example import wind_chill, heat_index
from pytest import approx
import pytest


def test_wind_chill():
    """Verify that the wind_chill function works correctly.
    Parameters: none
    Return: nothing
    """
    chill = wind_chill(0, 3)
    assert chill == approx(-6.9)

    chill = wind_chill(-5, 5)
    assert chill == approx(-16.4)

    chill = wind_chill(-10, 3)
    assert chill == approx(-18.2)


def test_heat_index():
    """Verify that the heat_index function works correctly.
    Parameters: none
    Return: nothing
    """
    assert heat_index(80, 80) == approx(84.2)
    assert heat_index(85, 80) == approx(96.8)
    assert heat_index(96, 70) == approx(126.4)


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
