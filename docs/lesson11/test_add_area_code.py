from add_area_code import add_area_code
import pytest

def test_add_area_code():
    test_cases = [
        ("801-412-3210", "801-412-3210"),
        ("656-4771", "208-656-4771")
    ]
    for original, expected in test_cases:
        assert add_area_code(original) == expected

pytest.main(["test_add_area_code.py"])
