from chemistry import get_name, get_atomic_mass, \
        parse_formula, molar_mass, FormulaError
from pytest import approx
import pytest
import math


def test_names():
    """Test the chemistry.get_name function."""
    # TODO: write this function.
    pass


def test_atomic_masses():
    """Test the chemistry.get_atomic_mass function."""
    # TODO: write this function.
    pass


def test_parse():
    """Test the chemistry.parse_formula function."""
    # TODO: write this function.
    pass


def test_molar_mass():
    """Test the chemistry.molar_mass function."""
    sym_quant_dict = parse_formula("H2O")
    assert molar_mass(sym_quant_dict) == approx(18.01528)

    sym_quant_dict = parse_formula("C6H6")
    assert molar_mass(sym_quant_dict) == approx(78.11184)

    sym_quant_dict = parse_formula("PO4H2(CH2)12CH3")
    assert molar_mass(sym_quant_dict) == approx(280.34072)


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["test_chemistry.py"])
