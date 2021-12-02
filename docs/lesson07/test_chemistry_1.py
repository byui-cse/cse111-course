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
    # periodic table in a variable named period_table_list.
    periodic_table_list = make_periodic_table()
    assert isinstance(periodic_table_list, list), \
        "make_periodic_table must return a list"

    # Create a key function that will be used by the sorted method.
    by_name = lambda element: element[NAME_INDEX]

    # Sort the periodic table by the element names.
    periodic_table_list = sorted(periodic_table_list, key=by_name)

    # Check each element in the sorted periodic table.
    i = 0
    element = periodic_table_list[i]
    check_element(element, ['Ac', 'Actinium', 227])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Al', 'Aluminum', 26.9815386])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Sb', 'Antimony', 121.76])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ar', 'Argon', 39.948])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['As', 'Arsenic', 74.9216])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['At', 'Astatine', 210])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ba', 'Barium', 137.327])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Be', 'Beryllium', 9.012182])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Bi', 'Bismuth', 208.9804])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['B', 'Boron', 10.811])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Br', 'Bromine', 79.904])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Cd', 'Cadmium', 112.411])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ca', 'Calcium', 40.078])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['C', 'Carbon', 12.0107])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ce', 'Cerium', 140.116])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Cs', 'Cesium', 132.9054519])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Cl', 'Chlorine', 35.453])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Cr', 'Chromium', 51.9961])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Co', 'Cobalt', 58.933195])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Cu', 'Copper', 63.546])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Dy', 'Dysprosium', 162.5])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Er', 'Erbium', 167.259])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Eu', 'Europium', 151.964])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['F', 'Fluorine', 18.9984032])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Fr', 'Francium', 223])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Gd', 'Gadolinium', 157.25])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ga', 'Gallium', 69.723])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ge', 'Germanium', 72.64])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Au', 'Gold', 196.966569])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Hf', 'Hafnium', 178.49])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['He', 'Helium', 4.002602])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ho', 'Holmium', 164.93032])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['H', 'Hydrogen', 1.00794])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['In', 'Indium', 114.818])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['I', 'Iodine', 126.90447])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ir', 'Iridium', 192.217])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Fe', 'Iron', 55.845])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Kr', 'Krypton', 83.798])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['La', 'Lanthanum', 138.90547])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Pb', 'Lead', 207.2])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Li', 'Lithium', 6.941])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Lu', 'Lutetium', 174.9668])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Mg', 'Magnesium', 24.305])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Mn', 'Manganese', 54.938045])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Hg', 'Mercury', 200.59])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Mo', 'Molybdenum', 95.96])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Nd', 'Neodymium', 144.242])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ne', 'Neon', 20.1797])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Np', 'Neptunium', 237])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ni', 'Nickel', 58.6934])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Nb', 'Niobium', 92.90638])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['N', 'Nitrogen', 14.0067])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Os', 'Osmium', 190.23])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['O', 'Oxygen', 15.9994])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Pd', 'Palladium', 106.42])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['P', 'Phosphorus', 30.973762])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Pt', 'Platinum', 195.084])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Pu', 'Plutonium', 244])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Po', 'Polonium', 209])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['K', 'Potassium', 39.0983])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Pr', 'Praseodymium', 140.90765])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Pm', 'Promethium', 145])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Pa', 'Protactinium', 231.03588])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ra', 'Radium', 226])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Rn', 'Radon', 222])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Re', 'Rhenium', 186.207])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Rh', 'Rhodium', 102.9055])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Rb', 'Rubidium', 85.4678])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ru', 'Ruthenium', 101.07])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Sm', 'Samarium', 150.36])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Sc', 'Scandium', 44.955912])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Se', 'Selenium', 78.96])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Si', 'Silicon', 28.0855])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ag', 'Silver', 107.8682])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Na', 'Sodium', 22.98976928])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Sr', 'Strontium', 87.62])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['S', 'Sulfur', 32.065])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ta', 'Tantalum', 180.94788])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Tc', 'Technetium', 98])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Te', 'Tellurium', 127.6])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Tb', 'Terbium', 158.92535])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Tl', 'Thallium', 204.3833])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Th', 'Thorium', 232.03806])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Tm', 'Thulium', 168.93421])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Sn', 'Tin', 118.71])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Ti', 'Titanium', 47.867])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['W', 'Tungsten', 183.84])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['U', 'Uranium', 238.02891])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['V', 'Vanadium', 50.9415])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Xe', 'Xenon', 131.293])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Yb', 'Ytterbium', 173.054])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Y', 'Yttrium', 88.90585])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Zn', 'Zinc', 65.38])
    i += 1
    element = periodic_table_list[i]
    check_element(element, ['Zr', 'Zirconium', 91.224])


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
