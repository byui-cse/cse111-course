# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from chemistry import make_periodic_table
from pytest import approx
import pytest


# These are the indexes of the
# elements in the periodic table.
SYMBOL_INDEX = 0
NAME_INDEX = 1
ATOMIC_MASS_INDEX = 2


def test_make_periodic_table():
    """Verify that the make_periodic_table function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_periodic_table function and store the returned
    # periodic table in a variable named periodic_table_list.
    periodic_table_list = make_periodic_table()
    assert isinstance(periodic_table_list, list), \
        "make_periodic_table function must return a list:" \
        f" expected a list but found a {type(periodic_table_list)}"

    exp_data = (
        "Ac", "Actinium", 227,
        "Al", "Aluminum", 26.9815386,
        "Sb", "Antimony", 121.76,
        "Ar", "Argon", 39.948,
        "As", "Arsenic", 74.9216,
        "At", "Astatine", 210,
        "Ba", "Barium", 137.327,
        "Be", "Beryllium", 9.012182,
        "Bi", "Bismuth", 208.9804,
        "B", "Boron", 10.811,
        "Br", "Bromine", 79.904,
        "Cd", "Cadmium", 112.411,
        "Ca", "Calcium", 40.078,
        "C", "Carbon", 12.0107,
        "Ce", "Cerium", 140.116,
        "Cs", "Cesium", 132.9054519,
        "Cl", "Chlorine", 35.453,
        "Cr", "Chromium", 51.9961,
        "Co", "Cobalt", 58.933195,
        "Cu", "Copper", 63.546,
        "Dy", "Dysprosium", 162.5,
        "Er", "Erbium", 167.259,
        "Eu", "Europium", 151.964,
        "F", "Fluorine", 18.9984032,
        "Fr", "Francium", 223,
        "Gd", "Gadolinium", 157.25,
        "Ga", "Gallium", 69.723,
        "Ge", "Germanium", 72.64,
        "Au", "Gold", 196.966569,
        "Hf", "Hafnium", 178.49,
        "He", "Helium", 4.002602,
        "Ho", "Holmium", 164.93032,
        "H", "Hydrogen", 1.00794,
        "In", "Indium", 114.818,
        "I", "Iodine", 126.90447,
        "Ir", "Iridium", 192.217,
        "Fe", "Iron", 55.845,
        "Kr", "Krypton", 83.798,
        "La", "Lanthanum", 138.90547,
        "Pb", "Lead", 207.2,
        "Li", "Lithium", 6.941,
        "Lu", "Lutetium", 174.9668,
        "Mg", "Magnesium", 24.305,
        "Mn", "Manganese", 54.938045,
        "Hg", "Mercury", 200.59,
        "Mo", "Molybdenum", 95.96,
        "Nd", "Neodymium", 144.242,
        "Ne", "Neon", 20.1797,
        "Np", "Neptunium", 237,
        "Ni", "Nickel", 58.6934,
        "Nb", "Niobium", 92.90638,
        "N", "Nitrogen", 14.0067,
        "Os", "Osmium", 190.23,
        "O", "Oxygen", 15.9994,
        "Pd", "Palladium", 106.42,
        "P", "Phosphorus", 30.973762,
        "Pt", "Platinum", 195.084,
        "Pu", "Plutonium", 244,
        "Po", "Polonium", 209,
        "K", "Potassium", 39.0983,
        "Pr", "Praseodymium", 140.90765,
        "Pm", "Promethium", 145,
        "Pa", "Protactinium", 231.03588,
        "Ra", "Radium", 226,
        "Rn", "Radon", 222,
        "Re", "Rhenium", 186.207,
        "Rh", "Rhodium", 102.9055,
        "Rb", "Rubidium", 85.4678,
        "Ru", "Ruthenium", 101.07,
        "Sm", "Samarium", 150.36,
        "Sc", "Scandium", 44.955912,
        "Se", "Selenium", 78.96,
        "Si", "Silicon", 28.0855,
        "Ag", "Silver", 107.8682,
        "Na", "Sodium", 22.98976928,
        "Sr", "Strontium", 87.62,
        "S", "Sulfur", 32.065,
        "Ta", "Tantalum", 180.94788,
        "Tc", "Technetium", 98,
        "Te", "Tellurium", 127.6,
        "Tb", "Terbium", 158.92535,
        "Tl", "Thallium", 204.3833,
        "Th", "Thorium", 232.03806,
        "Tm", "Thulium", 168.93421,
        "Sn", "Tin", 118.71,
        "Ti", "Titanium", 47.867,
        "W", "Tungsten", 183.84,
        "U", "Uranium", 238.02891,
        "V", "Vanadium", 50.9415,
        "Xe", "Xenon", 131.293,
        "Yb", "Ytterbium", 173.054,
        "Y", "Yttrium", 88.90585,
        "Zn", "Zinc", 65.38,
        "Zr", "Zirconium", 91.224
    )

    exp_len = int(len(exp_data) / 3)
    act_len = len(periodic_table_list)
    assert act_len == exp_len, \
        "The list returned by the make_periodic_table function" \
        f" contains too {'few' if act_len < exp_len else 'many'}" \
        f" elements; expected {exp_len} but found {act_len} elements."

    # Create a key function that will be used by the sorted method.
    by_name = lambda element: element[NAME_INDEX]

    # Sort the periodic table by the element names.
    periodic_table_list = sorted(periodic_table_list, key=by_name)

    # Check each element in the sorted periodic table.
    for i in range(len(periodic_table_list)):
        part = i * 3
        check_element(periodic_table_list[i], exp_data[part : part+3])


def check_element(actual, expected):
    """Verify that the actual element that came from the
    periodic_table_list contains the same values as the
    expected element.

    Parameters
        actual: a list that came from the periodic_table_list.
        expected: a list that contains the expected values.
    Return: nothing
    """
    name = expected[NAME_INDEX]
    assert actual[NAME_INDEX] == name, \
         f"{name} is missing from the periodic table."

    # Verify that the element's symbol is correct.
    act_symbol = actual[SYMBOL_INDEX]
    exp_symbol = expected[SYMBOL_INDEX]
    assert act_symbol == exp_symbol, \
         f"wrong symbol for {name}: " \
         f"expected {exp_symbol} but found {act_symbol}."

    # Verify that the element's atomic mass is correct.
    act_mass = actual[ATOMIC_MASS_INDEX]
    exp_mass = expected[ATOMIC_MASS_INDEX]
    assert act_mass == approx(exp_mass), \
            f"wrong atomic mass for {name}: " \
            f"expected {exp_mass} but found {act_mass}"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
