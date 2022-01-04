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
    # Call the make_periodic_table and store the returned
    # periodic table in a variable named periodic_table_list.
    periodic_table_list = make_periodic_table()
    assert isinstance(periodic_table_list, list), \
        "make_periodic_table function must return a list:" \
        f" expected a list but found a {type(periodic_table_list)}"

    # Create a key function that will be used by the sorted method.
    by_name = lambda element: element[NAME_INDEX]

    # Sort the periodic table by the element names.
    periodic_table_list = sorted(periodic_table_list, key=by_name)

    # Check each element in the sorted periodic table.
    i = 0
    check_element(periodic_table_list[i], ['Ac', 'Actinium', 227])
    i += 1
    check_element(periodic_table_list[i], ['Al', 'Aluminum', 26.9815386])
    i += 1
    check_element(periodic_table_list[i], ['Sb', 'Antimony', 121.76])
    i += 1
    check_element(periodic_table_list[i], ['Ar', 'Argon', 39.948])
    i += 1
    check_element(periodic_table_list[i], ['As', 'Arsenic', 74.9216])
    i += 1
    check_element(periodic_table_list[i], ['At', 'Astatine', 210])
    i += 1
    check_element(periodic_table_list[i], ['Ba', 'Barium', 137.327])
    i += 1
    check_element(periodic_table_list[i], ['Be', 'Beryllium', 9.012182])
    i += 1
    check_element(periodic_table_list[i], ['Bi', 'Bismuth', 208.9804])
    i += 1
    check_element(periodic_table_list[i], ['B', 'Boron', 10.811])
    i += 1
    check_element(periodic_table_list[i], ['Br', 'Bromine', 79.904])
    i += 1
    check_element(periodic_table_list[i], ['Cd', 'Cadmium', 112.411])
    i += 1
    check_element(periodic_table_list[i], ['Ca', 'Calcium', 40.078])
    i += 1
    check_element(periodic_table_list[i], ['C', 'Carbon', 12.0107])
    i += 1
    check_element(periodic_table_list[i], ['Ce', 'Cerium', 140.116])
    i += 1
    check_element(periodic_table_list[i], ['Cs', 'Cesium', 132.9054519])
    i += 1
    check_element(periodic_table_list[i], ['Cl', 'Chlorine', 35.453])
    i += 1
    check_element(periodic_table_list[i], ['Cr', 'Chromium', 51.9961])
    i += 1
    check_element(periodic_table_list[i], ['Co', 'Cobalt', 58.933195])
    i += 1
    check_element(periodic_table_list[i], ['Cu', 'Copper', 63.546])
    i += 1
    check_element(periodic_table_list[i], ['Dy', 'Dysprosium', 162.5])
    i += 1
    check_element(periodic_table_list[i], ['Er', 'Erbium', 167.259])
    i += 1
    check_element(periodic_table_list[i], ['Eu', 'Europium', 151.964])
    i += 1
    check_element(periodic_table_list[i], ['F', 'Fluorine', 18.9984032])
    i += 1
    check_element(periodic_table_list[i], ['Fr', 'Francium', 223])
    i += 1
    check_element(periodic_table_list[i], ['Gd', 'Gadolinium', 157.25])
    i += 1
    check_element(periodic_table_list[i], ['Ga', 'Gallium', 69.723])
    i += 1
    check_element(periodic_table_list[i], ['Ge', 'Germanium', 72.64])
    i += 1
    check_element(periodic_table_list[i], ['Au', 'Gold', 196.966569])
    i += 1
    check_element(periodic_table_list[i], ['Hf', 'Hafnium', 178.49])
    i += 1
    check_element(periodic_table_list[i], ['He', 'Helium', 4.002602])
    i += 1
    check_element(periodic_table_list[i], ['Ho', 'Holmium', 164.93032])
    i += 1
    check_element(periodic_table_list[i], ['H', 'Hydrogen', 1.00794])
    i += 1
    check_element(periodic_table_list[i], ['In', 'Indium', 114.818])
    i += 1
    check_element(periodic_table_list[i], ['I', 'Iodine', 126.90447])
    i += 1
    check_element(periodic_table_list[i], ['Ir', 'Iridium', 192.217])
    i += 1
    check_element(periodic_table_list[i], ['Fe', 'Iron', 55.845])
    i += 1
    check_element(periodic_table_list[i], ['Kr', 'Krypton', 83.798])
    i += 1
    check_element(periodic_table_list[i], ['La', 'Lanthanum', 138.90547])
    i += 1
    check_element(periodic_table_list[i], ['Pb', 'Lead', 207.2])
    i += 1
    check_element(periodic_table_list[i], ['Li', 'Lithium', 6.941])
    i += 1
    check_element(periodic_table_list[i], ['Lu', 'Lutetium', 174.9668])
    i += 1
    check_element(periodic_table_list[i], ['Mg', 'Magnesium', 24.305])
    i += 1
    check_element(periodic_table_list[i], ['Mn', 'Manganese', 54.938045])
    i += 1
    check_element(periodic_table_list[i], ['Hg', 'Mercury', 200.59])
    i += 1
    check_element(periodic_table_list[i], ['Mo', 'Molybdenum', 95.96])
    i += 1
    check_element(periodic_table_list[i], ['Nd', 'Neodymium', 144.242])
    i += 1
    check_element(periodic_table_list[i], ['Ne', 'Neon', 20.1797])
    i += 1
    check_element(periodic_table_list[i], ['Np', 'Neptunium', 237])
    i += 1
    check_element(periodic_table_list[i], ['Ni', 'Nickel', 58.6934])
    i += 1
    check_element(periodic_table_list[i], ['Nb', 'Niobium', 92.90638])
    i += 1
    check_element(periodic_table_list[i], ['N', 'Nitrogen', 14.0067])
    i += 1
    check_element(periodic_table_list[i], ['Os', 'Osmium', 190.23])
    i += 1
    check_element(periodic_table_list[i], ['O', 'Oxygen', 15.9994])
    i += 1
    check_element(periodic_table_list[i], ['Pd', 'Palladium', 106.42])
    i += 1
    check_element(periodic_table_list[i], ['P', 'Phosphorus', 30.973762])
    i += 1
    check_element(periodic_table_list[i], ['Pt', 'Platinum', 195.084])
    i += 1
    check_element(periodic_table_list[i], ['Pu', 'Plutonium', 244])
    i += 1
    check_element(periodic_table_list[i], ['Po', 'Polonium', 209])
    i += 1
    check_element(periodic_table_list[i], ['K', 'Potassium', 39.0983])
    i += 1
    check_element(periodic_table_list[i], ['Pr', 'Praseodymium', 140.90765])
    i += 1
    check_element(periodic_table_list[i], ['Pm', 'Promethium', 145])
    i += 1
    check_element(periodic_table_list[i], ['Pa', 'Protactinium', 231.03588])
    i += 1
    check_element(periodic_table_list[i], ['Ra', 'Radium', 226])
    i += 1
    check_element(periodic_table_list[i], ['Rn', 'Radon', 222])
    i += 1
    check_element(periodic_table_list[i], ['Re', 'Rhenium', 186.207])
    i += 1
    check_element(periodic_table_list[i], ['Rh', 'Rhodium', 102.9055])
    i += 1
    check_element(periodic_table_list[i], ['Rb', 'Rubidium', 85.4678])
    i += 1
    check_element(periodic_table_list[i], ['Ru', 'Ruthenium', 101.07])
    i += 1
    check_element(periodic_table_list[i], ['Sm', 'Samarium', 150.36])
    i += 1
    check_element(periodic_table_list[i], ['Sc', 'Scandium', 44.955912])
    i += 1
    check_element(periodic_table_list[i], ['Se', 'Selenium', 78.96])
    i += 1
    check_element(periodic_table_list[i], ['Si', 'Silicon', 28.0855])
    i += 1
    check_element(periodic_table_list[i], ['Ag', 'Silver', 107.8682])
    i += 1
    check_element(periodic_table_list[i], ['Na', 'Sodium', 22.98976928])
    i += 1
    check_element(periodic_table_list[i], ['Sr', 'Strontium', 87.62])
    i += 1
    check_element(periodic_table_list[i], ['S', 'Sulfur', 32.065])
    i += 1
    check_element(periodic_table_list[i], ['Ta', 'Tantalum', 180.94788])
    i += 1
    check_element(periodic_table_list[i], ['Tc', 'Technetium', 98])
    i += 1
    check_element(periodic_table_list[i], ['Te', 'Tellurium', 127.6])
    i += 1
    check_element(periodic_table_list[i], ['Tb', 'Terbium', 158.92535])
    i += 1
    check_element(periodic_table_list[i], ['Tl', 'Thallium', 204.3833])
    i += 1
    check_element(periodic_table_list[i], ['Th', 'Thorium', 232.03806])
    i += 1
    check_element(periodic_table_list[i], ['Tm', 'Thulium', 168.93421])
    i += 1
    check_element(periodic_table_list[i], ['Sn', 'Tin', 118.71])
    i += 1
    check_element(periodic_table_list[i], ['Ti', 'Titanium', 47.867])
    i += 1
    check_element(periodic_table_list[i], ['W', 'Tungsten', 183.84])
    i += 1
    check_element(periodic_table_list[i], ['U', 'Uranium', 238.02891])
    i += 1
    check_element(periodic_table_list[i], ['V', 'Vanadium', 50.9415])
    i += 1
    check_element(periodic_table_list[i], ['Xe', 'Xenon', 131.293])
    i += 1
    check_element(periodic_table_list[i], ['Yb', 'Ytterbium', 173.054])
    i += 1
    check_element(periodic_table_list[i], ['Y', 'Yttrium', 88.90585])
    i += 1
    check_element(periodic_table_list[i], ['Zn', 'Zinc', 65.38])
    i += 1
    check_element(periodic_table_list[i], ['Zr', 'Zirconium', 91.224])


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
