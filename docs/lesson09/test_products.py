# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from receipt import read_products
from os import path
from tempfile import mktemp
from pytest import approx
import pytest


def test_read_products():
    """Verify that the read_products function works correctly.
    Parameters: none
    Return: nothing
    """
    # Verify that the read_products function uses its filename
    # parameter by doing the following:
    # 1. Get a filename for a file that doesn't exist.
    # 2. Call the read_products function with the filename.
    # 3. Verify that the open function inside the read_products
    #    function raises a FileNotFoundError.
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        read_products(filename)
        pytest.fail("read_products must use its filename parameter")

    # Call the read_products function and store the
    # returned dictionary in a variable named products_dict.
    filename = path.join(path.dirname(__file__), "products.csv")
    products_dict = read_products(filename)

    # Verify that the read_products function returns a dictionary.
    assert isinstance(products_dict, dict), \
        "read_products must return a dictionary"

    # Verify that the products dictionry contains exactly 16 items.
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
    length = len(actual_value)
    assert length >= 2, \
        f"value list for product {product_number} contains too few elements"
    assert length <= 3, \
        f"value list for product {product_number} contains too many elements"

    if length == 2:
        NAME_INDEX = 0
        PRICE_INDEX = 1
    else:
        NAME_INDEX = 1
        PRICE_INDEX = 2

    # Verify that the product's name is correct.
    act_name = actual_value[NAME_INDEX]
    exp_name = expected_value[0]
    assert act_name == exp_name, \
        f"wrong name for product {product_number}: " \
        f"expected {exp_name} but found {act_name}."

    # Verify that the product's price is correct.
    act_price = actual_value[PRICE_INDEX]
    exp_price = expected_value[1]
    assert act_price == approx(exp_price), \
        f"wrong price for product {product_number}: " \
        f"expected {exp_price} but found {act_price}."


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
