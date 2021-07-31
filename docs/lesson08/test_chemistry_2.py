# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

from chemistry import make_periodic_table, \
    parse_formula, compute_molar_mass, FormulaError
from pytest import approx
import pytest


# These are the indexes of the
# elements in the periodic table.
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1


def test_make_periodic_table():
    """Verify that the make_periodic_table function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_periodic_table function and store the returned
    # dictionary in a variable named periodic_table_dict.
    periodic_table_dict = make_periodic_table()

    # Check each item in the periodic table dictionary.
    check_element(periodic_table_dict["Ac"], ["Actinium", 227])
    check_element(periodic_table_dict["Ag"], ["Silver", 107.8682])
    check_element(periodic_table_dict["Al"], ["Aluminum", 26.9815386])
    check_element(periodic_table_dict["Am"], ["Americium", 243])
    check_element(periodic_table_dict["Ar"], ["Argon", 39.948])
    check_element(periodic_table_dict["As"], ["Arsenic", 74.9216])
    check_element(periodic_table_dict["At"], ["Astatine", 210])
    check_element(periodic_table_dict["Au"], ["Gold", 196.966569])
    check_element(periodic_table_dict["B"], ["Boron", 10.811])
    check_element(periodic_table_dict["Ba"], ["Barium", 137.327])
    check_element(periodic_table_dict["Be"], ["Beryllium", 9.012182])
    check_element(periodic_table_dict["Bh"], ["Bohrium", 272])
    check_element(periodic_table_dict["Bi"], ["Bismuth", 208.9804])
    check_element(periodic_table_dict["Bk"], ["Berkelium", 247])
    check_element(periodic_table_dict["Br"], ["Bromine", 79.904])
    check_element(periodic_table_dict["C"], ["Carbon", 12.0107])
    check_element(periodic_table_dict["Ca"], ["Calcium", 40.078])
    check_element(periodic_table_dict["Cd"], ["Cadmium", 112.411])
    check_element(periodic_table_dict["Ce"], ["Cerium", 140.116])
    check_element(periodic_table_dict["Cf"], ["Californium", 251])
    check_element(periodic_table_dict["Cl"], ["Chlorine", 35.453])
    check_element(periodic_table_dict["Cm"], ["Curium", 247])
    check_element(periodic_table_dict["Cn"], ["Copernicium", 285])
    check_element(periodic_table_dict["Co"], ["Cobalt", 58.933195])
    check_element(periodic_table_dict["Cr"], ["Chromium", 51.9961])
    check_element(periodic_table_dict["Cs"], ["Cesium", 132.9054519])
    check_element(periodic_table_dict["Cu"], ["Copper", 63.546])
    check_element(periodic_table_dict["Db"], ["Dubnium", 268])
    check_element(periodic_table_dict["Ds"], ["Darmstadtium", 281])
    check_element(periodic_table_dict["Dy"], ["Dysprosium", 162.5])
    check_element(periodic_table_dict["Er"], ["Erbium", 167.259])
    check_element(periodic_table_dict["Es"], ["Einsteinium", 252])
    check_element(periodic_table_dict["Eu"], ["Europium", 151.964])
    check_element(periodic_table_dict["F"], ["Fluorine", 18.9984032])
    check_element(periodic_table_dict["Fe"], ["Iron", 55.845])
    check_element(periodic_table_dict["Fl"], ["Flerovium", 289])
    check_element(periodic_table_dict["Fm"], ["Fermium", 257])
    check_element(periodic_table_dict["Fr"], ["Francium", 223])
    check_element(periodic_table_dict["Ga"], ["Gallium", 69.723])
    check_element(periodic_table_dict["Gd"], ["Gadolinium", 157.25])
    check_element(periodic_table_dict["Ge"], ["Germanium", 72.64])
    check_element(periodic_table_dict["H"], ["Hydrogen", 1.00794])
    check_element(periodic_table_dict["He"], ["Helium", 4.002602])
    check_element(periodic_table_dict["Hf"], ["Hafnium", 178.49])
    check_element(periodic_table_dict["Hg"], ["Mercury", 200.59])
    check_element(periodic_table_dict["Ho"], ["Holmium", 164.93032])
    check_element(periodic_table_dict["Hs"], ["Hassium", 270])
    check_element(periodic_table_dict["I"], ["Iodine", 126.90447])
    check_element(periodic_table_dict["In"], ["Indium", 114.818])
    check_element(periodic_table_dict["Ir"], ["Iridium", 192.217])
    check_element(periodic_table_dict["K"], ["Potassium", 39.0983])
    check_element(periodic_table_dict["Kr"], ["Krypton", 83.798])
    check_element(periodic_table_dict["La"], ["Lanthanum", 138.90547])
    check_element(periodic_table_dict["Li"], ["Lithium", 6.941])
    check_element(periodic_table_dict["Lr"], ["Lawrencium", 262])
    check_element(periodic_table_dict["Lu"], ["Lutetium", 174.9668])
    check_element(periodic_table_dict["Lv"], ["Livermorium", 293])
    check_element(periodic_table_dict["Mc"], ["Moscovium", 288])
    check_element(periodic_table_dict["Md"], ["Mendelevium", 258])
    check_element(periodic_table_dict["Mg"], ["Magnesium", 24.305])
    check_element(periodic_table_dict["Mn"], ["Manganese", 54.938045])
    check_element(periodic_table_dict["Mo"], ["Molybdenum", 95.96])
    check_element(periodic_table_dict["Mt"], ["Meitnerium", 276])
    check_element(periodic_table_dict["N"], ["Nitrogen", 14.0067])
    check_element(periodic_table_dict["Na"], ["Sodium", 22.98976928])
    check_element(periodic_table_dict["Nb"], ["Niobium", 92.90638])
    check_element(periodic_table_dict["Nd"], ["Neodymium", 144.242])
    check_element(periodic_table_dict["Ne"], ["Neon", 20.1797])
    check_element(periodic_table_dict["Nh"], ["Nihonium", 284])
    check_element(periodic_table_dict["Ni"], ["Nickel", 58.6934])
    check_element(periodic_table_dict["No"], ["Nobelium", 259])
    check_element(periodic_table_dict["Np"], ["Neptunium", 237])
    check_element(periodic_table_dict["O"], ["Oxygen", 15.9994])
    check_element(periodic_table_dict["Og"], ["Oganesson", 294])
    check_element(periodic_table_dict["Os"], ["Osmium", 190.23])
    check_element(periodic_table_dict["P"], ["Phosphorus", 30.973762])
    check_element(periodic_table_dict["Pa"], ["Protactinium", 231.03588])
    check_element(periodic_table_dict["Pb"], ["Lead", 207.2])
    check_element(periodic_table_dict["Pd"], ["Palladium", 106.42])
    check_element(periodic_table_dict["Pm"], ["Promethium", 145])
    check_element(periodic_table_dict["Po"], ["Polonium", 209])
    check_element(periodic_table_dict["Pr"], ["Praseodymium", 140.90765])
    check_element(periodic_table_dict["Pt"], ["Platinum", 195.084])
    check_element(periodic_table_dict["Pu"], ["Plutonium", 244])
    check_element(periodic_table_dict["Ra"], ["Radium", 226])
    check_element(periodic_table_dict["Rb"], ["Rubidium", 85.4678])
    check_element(periodic_table_dict["Re"], ["Rhenium", 186.207])
    check_element(periodic_table_dict["Rf"], ["Rutherfordium", 267])
    check_element(periodic_table_dict["Rg"], ["Roentgenium", 280])
    check_element(periodic_table_dict["Rh"], ["Rhodium", 102.9055])
    check_element(periodic_table_dict["Rn"], ["Radon", 222])
    check_element(periodic_table_dict["Ru"], ["Ruthenium", 101.07])
    check_element(periodic_table_dict["S"], ["Sulfur", 32.065])
    check_element(periodic_table_dict["Sb"], ["Antimony", 121.76])
    check_element(periodic_table_dict["Sc"], ["Scandium", 44.955912])
    check_element(periodic_table_dict["Se"], ["Selenium", 78.96])
    check_element(periodic_table_dict["Sg"], ["Seaborgium", 271])
    check_element(periodic_table_dict["Si"], ["Silicon", 28.0855])
    check_element(periodic_table_dict["Sm"], ["Samarium", 150.36])
    check_element(periodic_table_dict["Sn"], ["Tin", 118.71])
    check_element(periodic_table_dict["Sr"], ["Strontium", 87.62])
    check_element(periodic_table_dict["Ta"], ["Tantalum", 180.94788])
    check_element(periodic_table_dict["Tb"], ["Terbium", 158.92535])
    check_element(periodic_table_dict["Tc"], ["Technetium", 98])
    check_element(periodic_table_dict["Te"], ["Tellurium", 127.6])
    check_element(periodic_table_dict["Th"], ["Thorium", 232.03806])
    check_element(periodic_table_dict["Ti"], ["Titanium", 47.867])
    check_element(periodic_table_dict["Tl"], ["Thallium", 204.3833])
    check_element(periodic_table_dict["Tm"], ["Thulium", 168.93421])
    check_element(periodic_table_dict["Ts"], ["Tennessine", 294])
    check_element(periodic_table_dict["U"], ["Uranium", 238.02891])
    check_element(periodic_table_dict["V"], ["Vanadium", 50.9415])
    check_element(periodic_table_dict["W"], ["Tungsten", 183.84])
    check_element(periodic_table_dict["Xe"], ["Xenon", 131.293])
    check_element(periodic_table_dict["Y"], ["Yttrium", 88.90585])
    check_element(periodic_table_dict["Yb"], ["Ytterbium", 173.054])
    check_element(periodic_table_dict["Zn"], ["Zinc", 65.38])
    check_element(periodic_table_dict["Zr"], ["Zirconium", 91.224])


def check_element(actual, expected):
    """Verify that the actual element that came from the
    periodic_table_dict contains the same values as the expected element.

    Parameters
        actual: a list that came from the periodic_table_dict.
        expected: a list that contains the expected values.
    Return: nothing
    """
    assert actual[NAME_INDEX] == expected[NAME_INDEX]
    assert actual[ATOMIC_MASS_INDEX] == approx(expected[ATOMIC_MASS_INDEX])


def test_parse_formula():
    """Test the chemistry.parse_formula function."""
    periodic_table_dict = make_periodic_table()

    assert parse_formula("H2O", periodic_table_dict) == [("H",2), ("O",1)]
    assert parse_formula("C6H6", periodic_table_dict) == [("C",6), ("H",6)]
    assert parse_formula("(C2(NaCl)4H2)2C4Na", periodic_table_dict) == [("C",8), ("Na",9), ("Cl",8), ("H",4)]
    with pytest.raises(FormulaError):
        parse_formula("L", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("4H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2L4", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("-H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("(H2O", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2)O3", periodic_table_dict)


def test_compute_molar_mass():
    """Test the chemistry.compute_molar_mass function."""
    periodic_table_dict = make_periodic_table()

    assert compute_molar_mass([], periodic_table_dict) == 0
    assert compute_molar_mass([["O",2]], periodic_table_dict) == approx(31.9988)
    assert compute_molar_mass([["C",6],["H",6]], periodic_table_dict) == approx(78.11184)
    assert compute_molar_mass([["C",13],["H",16],["N",2],["O",2]], periodic_table_dict) == approx(232.27834)


pytest.main(["-v", "--tb=line", "-rN", "test_chemistry_2.py"])
