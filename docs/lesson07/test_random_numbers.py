# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

from random_numbers import append_random_numbers
# from random_numbers import append_random_words
import pytest


def test_append_random_numbers():
    """Verify that the append_random_numbers function works correctly.
    Parameters: none
    Return: nothing
    """
    # Create an empty list named randnums.
    randnums = []

    # Verify that the length of the empty list is zero.
    assert len(randnums) == 0

    # Call the append_random_numbers function to append one number..
    append_random_numbers(randnums)

    # Verify that the randnums list now has one element.
    assert len(randnums) == 1

    # Verify that all the elements in the randnums list
    # are floating point numbers.
    for x in randnums:
        assert isinstance(x, float)

    # Call the append_random_numbers function to append three numbers.
    append_random_numbers(randnums, 3)

    # Verify that the randnums list now has four elements.
    assert len(randnums) == 4

    # Verify that all the elements in the randnums list
    # are floating point numbers.
    for x in randnums:
        assert isinstance(x, float)


#def test_append_random_words():
#    """Verify that the append_random_words function works correctly.
#    Parameters: none
#    Return: nothing
#    """
#    randwords = []
#    assert len(randwords) == 0
#
#    append_random_words(randwords)
#    assert len(randwords) == 1
#    for word in randwords:
#        assert isinstance(word, str)
#        assert len(word) >= 1
#
#    append_random_words(randwords, 3)
#    assert len(randwords) == 4
#    for word in randwords:
#        assert isinstance(word, str)
#        assert len(word) >= 1


pytest.main(["-v", "--tb=line", "-rN", __file__])
