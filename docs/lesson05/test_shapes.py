"""
Use all or any part of this file as a demonstration of writing test
functions during class in your section of CSE 111.

You could retain the numbered comments and delete all or any parts of
the code. Then give the modified file to your students and ask them to
write the code for the numbered comments. Or you could write the code
for the numbered comments with them as a demonstration during class.

Copyright 2020, Brigham Young University - Idaho. All rights reserved.
"""
import pytest
from pytest import approx
import math

from shapes import circle_circumference, circle_area, \
    triangle_perimeter, triangle_area


# 1. Write a test function that verifies that the
# circle_circumference function returns correct results.


# 2. Write a test function that verifies that the
# circle_area function returns correct results.


# 3. Write a test function that verifies that the
# triangle_perimeter function returns correct results.


# 4. Write a test function that verifies that the
# triangle_area function returns correct results.


# 5. Write test functions that verify that any of the other
# functions in the shapes.py file returns correct results.


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
