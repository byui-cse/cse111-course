# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from add_area_code import add_area_code
import pytest

def test_add_area_code():
    """Verify that the add_area_code function works correctly.
    Parameters: none
    Return: nothing
    """
    old_phone = "656-4771"
    new_phone = add_area_code(old_phone)

    # Verify that the add_area_code function returned a string.
    assert isinstance(new_phone, str), \
        f"add_area_code function failed to return a string for {old_phone}"

    # Verify that the add_area_code function
    # returned the correct value.
    assert new_phone == "208-656-4771"

    old_phone = "801-412-3210"
    new_phone = add_area_code(old_phone)

    # Verify that the add_area_code function returned a string.
    assert isinstance(new_phone, str), \
        f"add_area_code function failed to return a string for {old_phone}"

    # Verify that the add_area_code function
    # returned the correct value.
    assert new_phone == old_phone


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
