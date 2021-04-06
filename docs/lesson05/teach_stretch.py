from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract_city function returns correct results."""
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    assert extract_city("1700 Lincoln Rd, Idaho Falls, ID 83401") == "Idaho Falls"

def test_extract_state():
    """Verify that the extract_state function returns correct results."""
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    assert extract_state("1700 Lincoln Rd, Idaho Falls, ID 83401") == "ID"

def test_extract_zipcode():
    """Verify that the extract_zipcode function returns correct results."""
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440"
    assert extract_zipcode("1700 Lincoln Rd, Idaho Falls, ID 83401") == "83401"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "teach_stretch.py"])
