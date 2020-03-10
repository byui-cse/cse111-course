from chemistry import get_name, get_atomic_mass, parse_formula, molar_mass, FormulaError
import math
import pytest


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
    assert molar_mass(parse_formula("H2O")) == 18.01528
    assert molar_mass(parse_formula("C6H6")) == 78.11184
    assert math.isclose(molar_mass(parse_formula("PO4H2(CH2)12CH3")),
            280.34072, rel_tol=1e-5)
