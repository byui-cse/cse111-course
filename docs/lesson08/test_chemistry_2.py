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
    # Call the make_periodic_table and store the returned
    # periodic table in a variable named period_table.
    periodic_table = make_periodic_table()

    # Check each element in the sorted periodic table.
    check_element(periodic_table["Ac"], ["Actinium", 227])
    check_element(periodic_table["Ag"], ["Silver", 107.8682])
    check_element(periodic_table["Al"], ["Aluminum", 26.9815386])
    check_element(periodic_table["Am"], ["Americium", 243])
    check_element(periodic_table["Ar"], ["Argon", 39.948])
    check_element(periodic_table["As"], ["Arsenic", 74.9216])
    check_element(periodic_table["At"], ["Astatine", 210])
    check_element(periodic_table["Au"], ["Gold", 196.966569])
    check_element(periodic_table["B"], ["Boron", 10.811])
    check_element(periodic_table["Ba"], ["Barium", 137.327])
    check_element(periodic_table["Be"], ["Beryllium", 9.012182])
    check_element(periodic_table["Bh"], ["Bohrium", 272])
    check_element(periodic_table["Bi"], ["Bismuth", 208.9804])
    check_element(periodic_table["Bk"], ["Berkelium", 247])
    check_element(periodic_table["Br"], ["Bromine", 79.904])
    check_element(periodic_table["C"], ["Carbon", 12.0107])
    check_element(periodic_table["Ca"], ["Calcium", 40.078])
    check_element(periodic_table["Cd"], ["Cadmium", 112.411])
    check_element(periodic_table["Ce"], ["Cerium", 140.116])
    check_element(periodic_table["Cf"], ["Californium", 251])
    check_element(periodic_table["Cl"], ["Chlorine", 35.453])
    check_element(periodic_table["Cm"], ["Curium", 247])
    check_element(periodic_table["Cn"], ["Copernicium", 285])
    check_element(periodic_table["Co"], ["Cobalt", 58.933195])
    check_element(periodic_table["Cr"], ["Chromium", 51.9961])
    check_element(periodic_table["Cs"], ["Cesium", 132.9054519])
    check_element(periodic_table["Cu"], ["Copper", 63.546])
    check_element(periodic_table["Db"], ["Dubnium", 268])
    check_element(periodic_table["Ds"], ["Darmstadtium", 281])
    check_element(periodic_table["Dy"], ["Dysprosium", 162.5])
    check_element(periodic_table["Er"], ["Erbium", 167.259])
    check_element(periodic_table["Es"], ["Einsteinium", 252])
    check_element(periodic_table["Eu"], ["Europium", 151.964])
    check_element(periodic_table["F"], ["Fluorine", 18.9984032])
    check_element(periodic_table["Fe"], ["Iron", 55.845])
    check_element(periodic_table["Fl"], ["Flerovium", 289])
    check_element(periodic_table["Fm"], ["Fermium", 257])
    check_element(periodic_table["Fr"], ["Francium", 223])
    check_element(periodic_table["Ga"], ["Gallium", 69.723])
    check_element(periodic_table["Gd"], ["Gadolinium", 157.25])
    check_element(periodic_table["Ge"], ["Germanium", 72.64])
    check_element(periodic_table["H"], ["Hydrogen", 1.00794])
    check_element(periodic_table["He"], ["Helium", 4.002602])
    check_element(periodic_table["Hf"], ["Hafnium", 178.49])
    check_element(periodic_table["Hg"], ["Mercury", 200.59])
    check_element(periodic_table["Ho"], ["Holmium", 164.93032])
    check_element(periodic_table["Hs"], ["Hassium", 270])
    check_element(periodic_table["I"], ["Iodine", 126.90447])
    check_element(periodic_table["In"], ["Indium", 114.818])
    check_element(periodic_table["Ir"], ["Iridium", 192.217])
    check_element(periodic_table["K"], ["Potassium", 39.0983])
    check_element(periodic_table["Kr"], ["Krypton", 83.798])
    check_element(periodic_table["La"], ["Lanthanum", 138.90547])
    check_element(periodic_table["Li"], ["Lithium", 6.941])
    check_element(periodic_table["Lr"], ["Lawrencium", 262])
    check_element(periodic_table["Lu"], ["Lutetium", 174.9668])
    check_element(periodic_table["Lv"], ["Livermorium", 293])
    check_element(periodic_table["Mc"], ["Moscovium", 288])
    check_element(periodic_table["Md"], ["Mendelevium", 258])
    check_element(periodic_table["Mg"], ["Magnesium", 24.305])
    check_element(periodic_table["Mn"], ["Manganese", 54.938045])
    check_element(periodic_table["Mo"], ["Molybdenum", 95.96])
    check_element(periodic_table["Mt"], ["Meitnerium", 276])
    check_element(periodic_table["N"], ["Nitrogen", 14.0067])
    check_element(periodic_table["Na"], ["Sodium", 22.98976928])
    check_element(periodic_table["Nb"], ["Niobium", 92.90638])
    check_element(periodic_table["Nd"], ["Neodymium", 144.242])
    check_element(periodic_table["Ne"], ["Neon", 20.1797])
    check_element(periodic_table["Nh"], ["Nihonium", 284])
    check_element(periodic_table["Ni"], ["Nickel", 58.6934])
    check_element(periodic_table["No"], ["Nobelium", 259])
    check_element(periodic_table["Np"], ["Neptunium", 237])
    check_element(periodic_table["O"], ["Oxygen", 15.9994])
    check_element(periodic_table["Og"], ["Oganesson", 294])
    check_element(periodic_table["Os"], ["Osmium", 190.23])
    check_element(periodic_table["P"], ["Phosphorus", 30.973762])
    check_element(periodic_table["Pa"], ["Protactinium", 231.03588])
    check_element(periodic_table["Pb"], ["Lead", 207.2])
    check_element(periodic_table["Pd"], ["Palladium", 106.42])
    check_element(periodic_table["Pm"], ["Promethium", 145])
    check_element(periodic_table["Po"], ["Polonium", 209])
    check_element(periodic_table["Pr"], ["Praseodymium", 140.90765])
    check_element(periodic_table["Pt"], ["Platinum", 195.084])
    check_element(periodic_table["Pu"], ["Plutonium", 244])
    check_element(periodic_table["Ra"], ["Radium", 226])
    check_element(periodic_table["Rb"], ["Rubidium", 85.4678])
    check_element(periodic_table["Re"], ["Rhenium", 186.207])
    check_element(periodic_table["Rf"], ["Rutherfordium", 267])
    check_element(periodic_table["Rg"], ["Roentgenium", 280])
    check_element(periodic_table["Rh"], ["Rhodium", 102.9055])
    check_element(periodic_table["Rn"], ["Radon", 222])
    check_element(periodic_table["Ru"], ["Ruthenium", 101.07])
    check_element(periodic_table["S"], ["Sulfur", 32.065])
    check_element(periodic_table["Sb"], ["Antimony", 121.76])
    check_element(periodic_table["Sc"], ["Scandium", 44.955912])
    check_element(periodic_table["Se"], ["Selenium", 78.96])
    check_element(periodic_table["Sg"], ["Seaborgium", 271])
    check_element(periodic_table["Si"], ["Silicon", 28.0855])
    check_element(periodic_table["Sm"], ["Samarium", 150.36])
    check_element(periodic_table["Sn"], ["Tin", 118.71])
    check_element(periodic_table["Sr"], ["Strontium", 87.62])
    check_element(periodic_table["Ta"], ["Tantalum", 180.94788])
    check_element(periodic_table["Tb"], ["Terbium", 158.92535])
    check_element(periodic_table["Tc"], ["Technetium", 98])
    check_element(periodic_table["Te"], ["Tellurium", 127.6])
    check_element(periodic_table["Th"], ["Thorium", 232.03806])
    check_element(periodic_table["Ti"], ["Titanium", 47.867])
    check_element(periodic_table["Tl"], ["Thallium", 204.3833])
    check_element(periodic_table["Tm"], ["Thulium", 168.93421])
    check_element(periodic_table["Ts"], ["Tennessine", 294])
    check_element(periodic_table["U"], ["Uranium", 238.02891])
    check_element(periodic_table["V"], ["Vanadium", 50.9415])
    check_element(periodic_table["W"], ["Tungsten", 183.84])
    check_element(periodic_table["Xe"], ["Xenon", 131.293])
    check_element(periodic_table["Y"], ["Yttrium", 88.90585])
    check_element(periodic_table["Yb"], ["Ytterbium", 173.054])
    check_element(periodic_table["Zn"], ["Zinc", 65.38])
    check_element(periodic_table["Zr"], ["Zirconium", 91.224])


def check_element(actual, expected):
    """Verify that the actual element that came from the
    periodic_table contains the same values as the expected element.

    Parameters
        actual: a list that came from the periodic_table.
        expected: a list that contains the expected values.
    Return: nothing
    """
    assert actual[NAME_INDEX] == expected[NAME_INDEX]
    assert actual[ATOMIC_MASS_INDEX] == approx(expected[ATOMIC_MASS_INDEX])


def test_parse_formula():
    """Test the chemistry.parse_formula function."""
    periodic_table = make_periodic_table()

    assert parse_formula("H2O", periodic_table) == [("H",2), ("O",1)]
    assert parse_formula("C6H6", periodic_table) == [("C",6), ("H",6)]
    assert parse_formula("(C2(NaCl)4H2)2C4Na", periodic_table) == [("C",8), ("Na",9), ("Cl",8), ("H",4)]
    with pytest.raises(FormulaError):
        parse_formula("L", periodic_table)
    with pytest.raises(FormulaError):
        parse_formula("4H", periodic_table)
    with pytest.raises(FormulaError):
        parse_formula("H2L4", periodic_table)
    with pytest.raises(FormulaError):
        parse_formula("-H", periodic_table)
    with pytest.raises(FormulaError):
        parse_formula("(H2O", periodic_table)
    with pytest.raises(FormulaError):
        parse_formula("H2)O3", periodic_table)


def test_compute_molar_mass():
    """Test the chemistry.compute_molar_mass function."""
    periodic_table = make_periodic_table()

    assert compute_molar_mass([], periodic_table) == 0
    assert compute_molar_mass([["O",2]], periodic_table) == approx(31.9988)
    assert compute_molar_mass([["C",13], ["H",16], ["N",2], ["O",2]], periodic_table) == approx(232.27834)


pytest.main(["-v", "--tb=no", "test_chemistry_2.py"])
