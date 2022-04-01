# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
Verify that the make_full_name, extract_family_name,
and extract_given_name functions work correctly.
"""

from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"
    assert make_full_name("James", "Madison") == "Madison; James"
    assert make_full_name("J", "Ng") == "Ng; J"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    """Verify that the extract_family_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Smith-Jones; Ava") == "Smith-Jones"
    assert extract_family_name("Madison; James") == "Madison"
    assert extract_family_name("Ng; J") == "Ng"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    """Verify that the extract_given_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_given_name("Smith-Jones; Ava") == "Ava"
    assert extract_given_name("Madison; James") == "James"
    assert extract_given_name("Ng; J") == "J"
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
