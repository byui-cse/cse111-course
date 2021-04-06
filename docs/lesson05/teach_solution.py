from names import make_full_name, extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function returns correct results."""
    assert make_full_name("Penelope", "Smith-Jones") == "Smith-Jones; Penelope"
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("J", "Ng") == "Ng; J"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    """Verify that the extract_family_name function returns correct results."""
    assert extract_family_name("Smith-Jones; Penelope") == "Smith-Jones"
    assert extract_family_name("Washington; George") == "Washington"
    assert extract_family_name("Ng; J") == "Ng"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    """Verify that the extract_given_name function returns correct results."""
    assert extract_given_name("Smith-Jones; Penelope") == "Penelope"
    assert extract_given_name("Washington; George") == "George"
    assert extract_given_name("Ng; J") == "J"
    assert extract_given_name("; ") == ""

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "teach_solution.py"])
