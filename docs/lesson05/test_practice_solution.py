# Copyright 2026, Brigham Young University-Idaho. All rights reserved.

"""
Verify that the fahr_from_cels, wind_chill,
and heat_index functions work correctly.
"""

import pytest
from pytest import approx
from practice import fahr_from_cels, wind_chill, heat_index


def test_fahr_from_cels():
    """Verify that the fahr_from_cels function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the fahr_from_cels function and verify that it returns a number.
    fahr = fahr_from_cels(20)
    assert isinstance(fahr, int) or isinstance(fahr, float), \
        "fahr_from_cels function must return a number"

    # Call the fahr_from_cels function three times, each time with
    # different arguments. Use an assert statement to verify that
    # the fahr_from_cels function returns the correct result each time.
    fahr = fahr_from_cels(20)
    assert fahr == approx(68)

    fahr = fahr_from_cels(0)
    assert fahr == approx(32)

    fahr = fahr_from_cels(-40)
    assert fahr == approx(-40)


def test_wind_chill():
    """Verify that the wind_chill function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the wind_chill function and verify that it returns a number.
    chill = wind_chill(0, 3)
    assert isinstance(chill, int) or isinstance(chill, float), \
        "wind_chill function must return a number"

    # Call the wind_chill function three times, each time with
    # different arguments. Use an assert statement to verify that
    # the wind_chill function returns the correct result each time.
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
    # Call the heat_index function and verify that it returns a number.
    index = heat_index(80, 80)
    assert isinstance(index, int) or isinstance(index, float), \
        "heat_index function must return a number"

    # Call the heat_index function three times, each time with
    # different arguments. Use an assert statement to verify that
    # the heat_index function returns the correct result each time.
    assert heat_index(80, 80) == approx(84.2)
    assert heat_index(85, 80) == approx(96.8)
    assert heat_index(96, 70) == approx(126.4)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
