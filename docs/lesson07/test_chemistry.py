from chemistry import get_name, get_atomic_mass, parse, molar_mass
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
    """Test the chemistry.parse function."""
    # TODO: write this function.
    pass


def test_molar_mass():
    """Test the chemistry.molar_mass function."""
    assert molar_mass(parse("H2O")) == 18.01528
    assert molar_mass(parse("C6H6")) == 78.11184
    assert math.isclose(molar_mass(parse("PO4H2(CH2)12CH3")),
            280.34072, rel_tol=1e-5)
