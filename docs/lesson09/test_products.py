# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

from receipt import read_products
from pytest import approx
import pytest


def test_read_products():
    """Verify that the read_producdts function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the read_products function and store the
    # returned dictionary in a variable named products_dict.
    products_dict = read_products("products.csv")
    assert len(products_dict) == 16

    # Check each item in the products dictionary.
    check_product(products_dict, "D150", ["1 gallon milk", 2.85])
    check_product(products_dict, "D083", ["1 cup yogurt", 0.75])
    check_product(products_dict, "D215", ["1 lb cheddar cheese", 3.35])
    check_product(products_dict, "P019", ["iceberg lettuce", 1.15])
    check_product(products_dict, "P020", ["green leaf lettuce", 1.79])
    check_product(products_dict, "P021", ["butterhead lettuce", 1.83])
    check_product(products_dict, "P025", ["8 oz arugula", 2.19])
    check_product(products_dict, "P143", ["1 lb baby carrots", 1.39])
    check_product(products_dict, "W231", ["32 oz granola", 3.21])
    check_product(products_dict, "W112", ["wheat bread", 2.55])
    check_product(products_dict, "C013", ["twix candy bar", 0.85])
    check_product(products_dict, "H001", ["8 rolls toilet tissue", 6.45])
    check_product(products_dict, "H014", ["facial tissue", 2.49])
    check_product(products_dict, "H020", ["aluminum foil", 2.39])
    check_product(products_dict, "H021", ["12 oz dish soap", 3.19])
    check_product(products_dict, "H025", ["toilet cleaner", 4.50])


def check_product(products_dict, product_number, expected_value):
    """Verify that the data for one product number stored in the
    products dictionary is correct.

    Parameters
        products_dict: a dictionary that contains product data
        product_number: the product number of the product that this
            function will verify
        expected_value: the data that should be in the products
            dictionary for the product_number
    Return: nothing
    """
    assert product_number in products_dict
    actual_value = products_dict[product_number]
    assert len(actual_value) == 2 or len(actual_value) == 3

    NAME_INDEX = 0
    PRICE_INDEX = 1
    if len(actual_value) == 3:
        NAME_INDEX = 1
        PRICE_INDEX = 2

    assert actual_value[NAME_INDEX] == expected_value[0]
    assert actual_value[PRICE_INDEX] == approx(expected_value[1])


pytest.main(["-v", "--tb=line", "-rN", "test_products.py"])
