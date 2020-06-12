from chemistry import get_name, get_atomic_mass, parse_formula, molar_mass, FormulaError
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
    assert molar_mass(parse_formula("H2O")) == approx(18.01528)
    assert molar_mass(parse_formula("C6H6")) == approx(78.11184)
    assert molar_mass(parse_formula("PO4H2(CH2)12CH3")) == approx(280.34072)


pytest.main(["test_chemistry.py"])
