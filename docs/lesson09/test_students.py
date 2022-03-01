# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from students import read_dict
from inspect import signature
from os import path
from tempfile import mktemp
import pytest


def test_read_dict():
    """Verify that the read_dict function works correctly.
    Parameters: none
    Return: nothing
    """
    I_NUMBER_INDEX = 0

    # Verify that the read_dict function uses its filename
    # parameter by doing the following:
    # 1. Get a filename for a file that doesn't exist.
    # 2. Call the read_dict function with the filename.
    # 3. Verify that the open function inside the read_dict
    #    function raises a FileNotFoundError.
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        call_read_dict(filename, I_NUMBER_INDEX)
        pytest.fail("read_dict function must use its filename parameter")

    # Call the read_dict function which will read the students.csv
    # file and create and return a dictinoary.
    filename = path.join(path.dirname(__file__), "students.csv")
    students_dict = call_read_dict(filename, I_NUMBER_INDEX)

    # Verify that the read_dict function returns a dictionary.
    assert isinstance(students_dict, dict), \
        "read_dict function must return a dictionary:" \
        f" expected a dictionary but found a {type(students_dict)}"

    # Verify that the students dictionary contains exactly nine items.
    length = len(students_dict)
    exp_len = 9
    assert length == exp_len, \
        "students dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"

    # Verify the correctness of the nine items in the dictionary.
    check_student(students_dict, "751766201", "James Smith")
    check_student(students_dict, "751762102", "Esther Einboden")
    check_student(students_dict, "052058203", "Cassidy Benavidez")
    check_student(students_dict, "323021604", "Joel Hatch")
    check_student(students_dict, "251041405", "Brianna Ririe")
    check_student(students_dict, "001152306", "Stefano Hisler")
    check_student(students_dict, "182706207", "Hyeonbeom Park")
    check_student(students_dict, "124712708", "Maren Thomas")
    check_student(students_dict, "212505409", "Tyler Clark")


def call_read_dict(filename, key_column_index):
    """Call the read_dict function with the correct number of
    parameters.
    """
    sig = signature(read_dict)
    length = len(sig.parameters)
    min_len = 1
    max_len = 2
    assert length == min_len or length == max_len, \
        f"The read_dict function contains too " \
        f"{'few' if length < min_len else 'many'} parameters; " \
        f"expected {min_len} or {max_len} parameters but found {length}"
    if length == min_len:
        dictionary = read_dict(filename)
    else:
        dictionary = read_dict(filename, key_column_index)
    return dictionary


def check_student(students_dict, inumber, exp_name):
    """Verify that the data for one student stored in the
    students dictionary is correct.

    Parameters
        students_dict: a dictionary that contains student data
        inumber: a student's I-Number that should be in the dictionary
        exp_name: the student's expected name
    Return: nothing
    """
    # Verify that inumber is in the students dictionary.
    assert inumber in students_dict, \
        f'"{inumber}" is missing from the students dictionary.'

    actual = students_dict[inumber]
    assert isinstance(actual, str) or isinstance(actual, list), \
        "Each value in the students dictionary must be either a string " \
        f"or a list. The value for {inumber} is of type {type(actual)} " \
        "which is not a string or a list."

    if isinstance(actual, str):
        # Verify that the student's name is correct.
        assert actual == exp_name, \
                f'Wrong name for "{inumber}"; ' \
                f'expected {exp_name} but found {actual}'
    else:
        length = len(actual)
        min_len = 1
        max_len = 2
        assert length == min_len or length == max_len, \
            f"The value list for student {inumber} contains too " \
            f"{'few' if length < min_len else 'many'} elements; " \
            f"expected {min_len} or {max_len} elements but found {length}"

        if length == min_len:
            # Verify that the student's name is correct.
            NAME_INDEX = 0
            act_name = actual[NAME_INDEX]
            assert act_name == exp_name, \
                    f'Wrong name for "{inumber}"; ' \
                    f'expected {exp_name} but found {act_name}'
        else:
            # Verify that the student's I-Number is correct.
            I_NUMBER_INDEX = 0
            act_inum = actual[I_NUMBER_INDEX]
            assert act_inum == inumber, \
                    'Inconsistent I-Numbers in the key and value. ' \
                    f'The key is {inumber} but {act_inum} is in ' \
                    'the corresponding value.'

            # Verify that the student's name is correct.
            NAME_INDEX = 1
            act_name = actual[NAME_INDEX]
            assert act_name == exp_name, \
                    f'Wrong name for "{inumber}"; ' \
                    f'expected {exp_name} but found {act_name}'


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
