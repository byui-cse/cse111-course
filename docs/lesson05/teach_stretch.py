# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
Verify that the extract_city, extract_state,
and extract_zipcode functions work correctly.
"""

from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract_city function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    assert extract_city("78 Pine St, Avon Park, FL 33825") == "Avon Park"


def test_extract_state():
    """Verify that the extract_state function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"


def test_extract_zipcode():
    """Verify that the extract_zipcode
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440"
    assert extract_zipcode("78 Pine St, Avon Park, FL 33825") == "33825"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
