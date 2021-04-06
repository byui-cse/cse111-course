# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

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
    # periodic table in a variable named period_table.
    periodic_table = make_periodic_table()

    # Create a key function that will be used by the sorted method.
    by_symbol = lambda element: element[SYMBOL_INDEX]

    # Sort the periodic table by the element symbols.
    periodic_table = sorted(periodic_table, key=by_symbol)

    # Check each element in the sorted periodic table.
    i = 0
    check_element(periodic_table[i], ["Ac", "Actinium", 227])
    i += 1
    check_element(periodic_table[i], ["Ag", "Silver", 107.8682])
    i += 1
    check_element(periodic_table[i], ["Al", "Aluminum", 26.9815386])
    i += 1
    check_element(periodic_table[i], ["Am", "Americium", 243])
    i += 1
    check_element(periodic_table[i], ["Ar", "Argon", 39.948])
    i += 1
    check_element(periodic_table[i], ["As", "Arsenic", 74.9216])
    i += 1
    check_element(periodic_table[i], ["At", "Astatine", 210])
    i += 1
    check_element(periodic_table[i], ["Au", "Gold", 196.966569])
    i += 1
    check_element(periodic_table[i], ["B", "Boron", 10.811])
    i += 1
    check_element(periodic_table[i], ["Ba", "Barium", 137.327])
    i += 1
    check_element(periodic_table[i], ["Be", "Beryllium", 9.012182])
    i += 1
    check_element(periodic_table[i], ["Bh", "Bohrium", 272])
    i += 1
    check_element(periodic_table[i], ["Bi", "Bismuth", 208.9804])
    i += 1
    check_element(periodic_table[i], ["Bk", "Berkelium", 247])
    i += 1
    check_element(periodic_table[i], ["Br", "Bromine", 79.904])
    i += 1
    check_element(periodic_table[i], ["C", "Carbon", 12.0107])
    i += 1
    check_element(periodic_table[i], ["Ca", "Calcium", 40.078])
    i += 1
    check_element(periodic_table[i], ["Cd", "Cadmium", 112.411])
    i += 1
    check_element(periodic_table[i], ["Ce", "Cerium", 140.116])
    i += 1
    check_element(periodic_table[i], ["Cf", "Californium", 251])
    i += 1
    check_element(periodic_table[i], ["Cl", "Chlorine", 35.453])
    i += 1
    check_element(periodic_table[i], ["Cm", "Curium", 247])
    i += 1
    check_element(periodic_table[i], ["Cn", "Copernicium", 285])
    i += 1
    check_element(periodic_table[i], ["Co", "Cobalt", 58.933195])
    i += 1
    check_element(periodic_table[i], ["Cr", "Chromium", 51.9961])
    i += 1
    check_element(periodic_table[i], ["Cs", "Cesium", 132.9054519])
    i += 1
    check_element(periodic_table[i], ["Cu", "Copper", 63.546])
    i += 1
    check_element(periodic_table[i], ["Db", "Dubnium", 268])
    i += 1
    check_element(periodic_table[i], ["Ds", "Darmstadtium", 281])
    i += 1
    check_element(periodic_table[i], ["Dy", "Dysprosium", 162.5])
    i += 1
    check_element(periodic_table[i], ["Er", "Erbium", 167.259])
    i += 1
    check_element(periodic_table[i], ["Es", "Einsteinium", 252])
    i += 1
    check_element(periodic_table[i], ["Eu", "Europium", 151.964])
    i += 1
    check_element(periodic_table[i], ["F", "Fluorine", 18.9984032])
    i += 1
    check_element(periodic_table[i], ["Fe", "Iron", 55.845])
    i += 1
    check_element(periodic_table[i], ["Fl", "Flerovium", 289])
    i += 1
    check_element(periodic_table[i], ["Fm", "Fermium", 257])
    i += 1
    check_element(periodic_table[i], ["Fr", "Francium", 223])
    i += 1
    check_element(periodic_table[i], ["Ga", "Gallium", 69.723])
    i += 1
    check_element(periodic_table[i], ["Gd", "Gadolinium", 157.25])
    i += 1
    check_element(periodic_table[i], ["Ge", "Germanium", 72.64])
    i += 1
    check_element(periodic_table[i], ["H", "Hydrogen", 1.00794])
    i += 1
    check_element(periodic_table[i], ["He", "Helium", 4.002602])
    i += 1
    check_element(periodic_table[i], ["Hf", "Hafnium", 178.49])
    i += 1
    check_element(periodic_table[i], ["Hg", "Mercury", 200.59])
    i += 1
    check_element(periodic_table[i], ["Ho", "Holmium", 164.93032])
    i += 1
    check_element(periodic_table[i], ["Hs", "Hassium", 270])
    i += 1
    check_element(periodic_table[i], ["I", "Iodine", 126.90447])
    i += 1
    check_element(periodic_table[i], ["In", "Indium", 114.818])
    i += 1
    check_element(periodic_table[i], ["Ir", "Iridium", 192.217])
    i += 1
    check_element(periodic_table[i], ["K", "Potassium", 39.0983])
    i += 1
    check_element(periodic_table[i], ["Kr", "Krypton", 83.798])
    i += 1
    check_element(periodic_table[i], ["La", "Lanthanum", 138.90547])
    i += 1
    check_element(periodic_table[i], ["Li", "Lithium", 6.941])
    i += 1
    check_element(periodic_table[i], ["Lr", "Lawrencium", 262])
    i += 1
    check_element(periodic_table[i], ["Lu", "Lutetium", 174.9668])
    i += 1
    check_element(periodic_table[i], ["Lv", "Livermorium", 293])
    i += 1
    check_element(periodic_table[i], ["Mc", "Moscovium", 288])
    i += 1
    check_element(periodic_table[i], ["Md", "Mendelevium", 258])
    i += 1
    check_element(periodic_table[i], ["Mg", "Magnesium", 24.305])
    i += 1
    check_element(periodic_table[i], ["Mn", "Manganese", 54.938045])
    i += 1
    check_element(periodic_table[i], ["Mo", "Molybdenum", 95.96])
    i += 1
    check_element(periodic_table[i], ["Mt", "Meitnerium", 276])
    i += 1
    check_element(periodic_table[i], ["N", "Nitrogen", 14.0067])
    i += 1
    check_element(periodic_table[i], ["Na", "Sodium", 22.98976928])
    i += 1
    check_element(periodic_table[i], ["Nb", "Niobium", 92.90638])
    i += 1
    check_element(periodic_table[i], ["Nd", "Neodymium", 144.242])
    i += 1
    check_element(periodic_table[i], ["Ne", "Neon", 20.1797])
    i += 1
    check_element(periodic_table[i], ["Nh", "Nihonium", 284])
    i += 1
    check_element(periodic_table[i], ["Ni", "Nickel", 58.6934])
    i += 1
    check_element(periodic_table[i], ["No", "Nobelium", 259])
    i += 1
    check_element(periodic_table[i], ["Np", "Neptunium", 237])
    i += 1
    check_element(periodic_table[i], ["O", "Oxygen", 15.9994])
    i += 1
    check_element(periodic_table[i], ["Og", "Oganesson", 294])
    i += 1
    check_element(periodic_table[i], ["Os", "Osmium", 190.23])
    i += 1
    check_element(periodic_table[i], ["P", "Phosphorus", 30.973762])
    i += 1
    check_element(periodic_table[i], ["Pa", "Protactinium", 231.03588])
    i += 1
    check_element(periodic_table[i], ["Pb", "Lead", 207.2])
    i += 1
    check_element(periodic_table[i], ["Pd", "Palladium", 106.42])
    i += 1
    check_element(periodic_table[i], ["Pm", "Promethium", 145])
    i += 1
    check_element(periodic_table[i], ["Po", "Polonium", 209])
    i += 1
    check_element(periodic_table[i], ["Pr", "Praseodymium", 140.90765])
    i += 1
    check_element(periodic_table[i], ["Pt", "Platinum", 195.084])
    i += 1
    check_element(periodic_table[i], ["Pu", "Plutonium", 244])
    i += 1
    check_element(periodic_table[i], ["Ra", "Radium", 226])
    i += 1
    check_element(periodic_table[i], ["Rb", "Rubidium", 85.4678])
    i += 1
    check_element(periodic_table[i], ["Re", "Rhenium", 186.207])
    i += 1
    check_element(periodic_table[i], ["Rf", "Rutherfordium", 267])
    i += 1
    check_element(periodic_table[i], ["Rg", "Roentgenium", 280])
    i += 1
    check_element(periodic_table[i], ["Rh", "Rhodium", 102.9055])
    i += 1
    check_element(periodic_table[i], ["Rn", "Radon", 222])
    i += 1
    check_element(periodic_table[i], ["Ru", "Ruthenium", 101.07])
    i += 1
    check_element(periodic_table[i], ["S", "Sulfur", 32.065])
    i += 1
    check_element(periodic_table[i], ["Sb", "Antimony", 121.76])
    i += 1
    check_element(periodic_table[i], ["Sc", "Scandium", 44.955912])
    i += 1
    check_element(periodic_table[i], ["Se", "Selenium", 78.96])
    i += 1
    check_element(periodic_table[i], ["Sg", "Seaborgium", 271])
    i += 1
    check_element(periodic_table[i], ["Si", "Silicon", 28.0855])
    i += 1
    check_element(periodic_table[i], ["Sm", "Samarium", 150.36])
    i += 1
    check_element(periodic_table[i], ["Sn", "Tin", 118.71])
    i += 1
    check_element(periodic_table[i], ["Sr", "Strontium", 87.62])
    i += 1
    check_element(periodic_table[i], ["Ta", "Tantalum", 180.94788])
    i += 1
    check_element(periodic_table[i], ["Tb", "Terbium", 158.92535])
    i += 1
    check_element(periodic_table[i], ["Tc", "Technetium", 98])
    i += 1
    check_element(periodic_table[i], ["Te", "Tellurium", 127.6])
    i += 1
    check_element(periodic_table[i], ["Th", "Thorium", 232.03806])
    i += 1
    check_element(periodic_table[i], ["Ti", "Titanium", 47.867])
    i += 1
    check_element(periodic_table[i], ["Tl", "Thallium", 204.3833])
    i += 1
    check_element(periodic_table[i], ["Tm", "Thulium", 168.93421])
    i += 1
    check_element(periodic_table[i], ["Ts", "Tennessine", 294])
    i += 1
    check_element(periodic_table[i], ["U", "Uranium", 238.02891])
    i += 1
    check_element(periodic_table[i], ["V", "Vanadium", 50.9415])
    i += 1
    check_element(periodic_table[i], ["W", "Tungsten", 183.84])
    i += 1
    check_element(periodic_table[i], ["Xe", "Xenon", 131.293])
    i += 1
    check_element(periodic_table[i], ["Y", "Yttrium", 88.90585])
    i += 1
    check_element(periodic_table[i], ["Yb", "Ytterbium", 173.054])
    i += 1
    check_element(periodic_table[i], ["Zn", "Zinc", 65.38])
    i += 1
    check_element(periodic_table[i], ["Zr", "Zirconium", 91.224])


def check_element(actual, expected):
    """Verify that the actual element that came from the
    periodic_table contains the same values as the expected element.

    Parameters
        actual: a list that came from the periodic_table.
        expected: a list that contains the expected values.
    Return: nothing
    """
    assert actual[SYMBOL_INDEX] == expected[SYMBOL_INDEX]
    assert actual[NAME_INDEX] == expected[NAME_INDEX]
    assert actual[ATOMIC_MASS_INDEX] == approx(expected[ATOMIC_MASS_INDEX])


pytest.main(["-v", "--tb=line", "-rN", "test_chemistry_1.py"])
