from students import read_dict
from os import path
import pytest


def test_read_dict():
    """Verify that the read_dict function works correctly.
    Parameters: none
    Return: nothing
    """
    I_NUMBER = 0

    # Call the read_dict function which will read the students.csv
    # file and create and return a dictinoary.
    filename = path.join(path.dirname(__file__), "students.csv")
    students = read_dict(filename, I_NUMBER)

    # Verify that the read_dict function returns a dictionary.
    assert isinstance(students, dict), \
        "read_dict must return a dictionary"

    # Verify that the students dictionary contains exactly nine items.
    assert len(students) == 9

    # Verify the correctness of the nine items in the dictionary.
    assert students["751766201"] == ["751766201", "James Smith"]
    assert students["751762102"] == ["751762102", "Esther Einboden"]
    assert students["052058203"] == ["052058203", "Cassidy Benavidez"]
    assert students["323021604"] == ["323021604", "Joel Hatch"]
    assert students["251041405"] == ["251041405", "Brianna Ririe"]
    assert students["001152306"] == ["001152306", "Stefano Hisler"]
    assert students["182706207"] == ["182706207", "Hyeonbeom Park"]
    assert students["124712708"] == ["124712708", "Maren Thomas"]
    assert students["212505409"] == ["212505409", "Tyler Clark"]


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
