from collections import namedtuple


def init_periodic_table():
    """Create, initialize, and return a dictionary
    that contains all known elements. Each key
    value pair in the dictionary is in this form:
    symbol : (name, symbol, atomic_mass)

    The unit for atomic mass is atomic mass
    units (amu) sometimes abbreviated as u
    """
    Element = namedtuple("Element", ["name", "symbol", "atomic_mass"])
    table = {}
    table["H"] = Element("Hydrogen", "H", 1.01)
    table["He"] = Element("Helium", "He", 4.002602)
    table["Li"] = Element("Lithium", "Li", 6.941)
    table["Be"] = Element("Beryllium", "Be", 9.012182)
    table["B"] = Element("Boron", "B", 10.811)
    table["C"] = Element("Carbon", "C", 12.01)
    table["N"] = Element("Nitrogen", "N", 14.0067)
    table["O"] = Element("Oxygen", "O", 15.9994)
    table["F"] = Element("Fluorine", "F", 18.9984032)
    table["Ne"] = Element("Neon", "Ne", 20.1797)
    table["Na"] = Element("Sodium", "Na", 22.98976928)
    table["Mg"] = Element("Magnesium", "Mg", 24.305)
    table["Al"] = Element("Aluminium", "Al", 26.9815386)
    table["Si"] = Element("Silicon", "Si", 28.0855)
    table["P"] = Element("Phosphorus", "P", 30.973762)
    table["S"] = Element("Sulfur", "S", 32.065)
    table["Cl"] = Element("Chlorine", "Cl", 35.453)
    table["Ar"] = Element("Argon", "Ar", 39.948)
    table["K"] = Element("Potassium", "K", 39.0983)
    table["Ca"] = Element("Calsium", "Ca", 40.078)
    table["Sc"] = Element("Scandium", "Sc", 44.955912)
    table["Ti"] = Element("Titanium", "Ti", 47.9)
    table["V"] = Element("Vanadium", "V", 50.9415)
    table["Cr"] = Element("Chromium", "Cr", 51.9961)
    table["Mn"] = Element("Manganese", "Mn", 54.938045)
    table["Fe"] = Element("Iron", "Fe", 55.845)
    table["Co"] = Element("Cobalt", "Co", 58.933195)
    table["Ni"] = Element("Nickel", "Ni", 58.6934)
    table["Cu"] = Element("Copper", "Cu", 63.546)
    table["Zn"] = Element("Zinc", "Zn", 65.38)
    table["Ga"] = Element("Gallium", "Ga", 69.723)
    table["Ge"] = Element("Germanium", "Ge", 72.64)
    table["As"] = Element("Arsenic", "As", 74.9216)
    table["Se"] = Element("Selenium", "Se", 78.96)
    table["Br"] = Element("Bromine", "Br", 79.904)
    table["Kr"] = Element("Krypton", "Kr", 83.798)
    table["Rb"] = Element("Rubidium", "Rb", 85.4678)
    table["Sr"] = Element("Strontium", "Sr", 87.62)
    table["Y"] = Element("Yttrium", "Y", 88.90585)
    table["Zr"] = Element("Zirconium", "Zr", 91.224)
    table["Nb"] = Element("Niobium", "Nb", 92.90638)
    table["Mo"] = Element("Molybdenum", "Mo", 95.96)
    table["Tc"] = Element("Technetium", "Tc", 98)
    table["Ru"] = Element("Ruthenium", "Ru", 101.07)
    table["Rh"] = Element("Rhodium", "Rh", 102.9055)
    table["Pd"] = Element("Palladium", "Pd", 106.42)
    table["Ag"] = Element("Silver", "Ag", 107.8682)
    table["Cd"] = Element("Cadmium", "Cd", 112.411)
    table["In"] = Element("Indium", "In", 114.818)
    table["Sn"] = Element("Tin", "Sn", 118.71)
    table["Sb"] = Element("Antimony", "Sb", 121.76)
    table["Te"] = Element("Tellurium", "Te", 127.6)
    table["I"] = Element("Iodine", "I", 126.90447)
    table["Xe"] = Element("Xenon", "Xe", 131.293)
    table["Cs"] = Element("Cesium", "Cs", 132.9054519)
    table["Ba"] = Element("Barium", "Ba", 137.327)
    table["La"] = Element("Lanthanum", "La", 138.90547)
    table["Ce"] = Element("Cerium", "Ce", 140.116)
    table["Pr"] = Element("Crazyname", "Pr", 140.90765)
    table["Nd"] = Element("Neodymium", "Nd", 144.242)
    table["Pm"] = Element("Promethium", "Pm", 145)
    table["Sm"] = Element("Samarium", "Sm", 150.36)
    table["Eu"] = Element("Europium", "Eu", 151.964)
    table["Gd"] = Element("Gadolinium", "Gd", 157.25)
    table["Tb"] = Element("Terbium", "Tb", 158.92535)
    table["Dy"] = Element("Dysprosium", "Dy", 162.5)
    table["Ho"] = Element("Holmium", "Ho", 164.93032)
    table["Er"] = Element("Erbium", "Er", 167.259)
    table["Tm"] = Element("Thulium", "Tm", 168.93421)
    table["Yb"] = Element("Ytterbium", "Yb", 173.054)
    table["Lu"] = Element("Lutetium", "Lu", 174.9668)
    table["Hf"] = Element("Hafnium", "Hf", 178.49)
    table["Ta"] = Element("Tantalum", "Ta", 180.94788)
    table["W"] = Element("Tungsten", "W", 183.84)
    table["Re"] = Element("Rhenium", "Re", 186.207)
    table["Os"] = Element("Osmium", "Os", 190.23)
    table["Ir"] = Element("Iridium", "Ir", 192.217)
    table["Pt"] = Element("Platinum", "Pt", 195.084)
    table["Au"] = Element("Gold", "Au", 196.966569)
    table["Hg"] = Element("Mercury", "Hg", 200.59)
    table["Tl"] = Element("Thallium", "Tl", 204.3833)
    table["Pb"] = Element("Lead", "Pb", 207.2)
    table["Bi"] = Element("Bismuth", "Bi", 208.9804)
    table["Po"] = Element("Polonium", "Po", 209)
    table["At"] = Element("Astatine", "At", 210)
    table["Rn"] = Element("Radon", "Rn", 222)
    table["Fr"] = Element("Francium", "Fr", 223)
    table["Ra"] = Element("Radium", "Ra", 226)
    table["Ac"] = Element("Actinium", "Ac", 227)
    table["Th"] = Element("Thorium", "Th", 232.03806)
    table["Pa"] = Element("Whonamedthis", "Pa", 231.03588)
    table["U"] = Element("Uranium", "U", 238.02891)
    table["Np"] = Element("Neptunium", "Np", 237)
    table["Pu"] = Element("Plutonium", "Pu", 244)
    table["Am"] = Element("Americium", "Am", 243)
    table["Cm"] = Element("Curium", "Cm", 247)
    table["Bk"] = Element("Berkelium", "Bk", 247)
    table["Cf"] = Element("Californium", "Cf", 251)
    table["Es"] = Element("Einsteinium", "Es", 252)
    table["Fm"] = Element("Fermium", "Fm", 257)
    table["Md"] = Element("Mendelevium", "Md", 258)
    table["No"] = Element("Nobelium", "No", 259)
    table["Lr"] = Element("Lawrencium", "Lr", 262)
    table["Rf"] = Element("Rutherfordium", "Rf", 267)
    table["Db"] = Element("Dubnium", "Db", 268)
    table["Sg"] = Element("Seaborgium", "Sg", 271)
    table["Bh"] = Element("Bohrium", "Bh", 272)
    table["Hs"] = Element("Hassium", "Hs", 270)
    table["Mt"] = Element("Meitnerium", "Mt", 276)
    table["Ds"] = Element("Darmstadtium", "Ds", 281)
    table["Rg"] = Element("Roentgenium", "Rg", 280)
    table["Cn"] = Element("Copernicium", "Cn", 285)
    table["Nh"] = Element("Nihonium", "Nh", 284)
    table["Fl"] = Element("Flerovium", "Fl", 289)
    table["Mc"] = Element("Moscovium", "Mc", 288)
    table["Lv"] = Element("Livermorium", "Lv", 293)
    table["Ts"] = Element("Tennessine", "Ts", 294)
    table["Og"] = Element("Oganesson", "Og", 294)
    return table


# A dictionary with global scope that stores
# information about the known elements.
periodic_table = init_periodic_table()


def get_name(symbol):
    """Return the name of an element."""
    return periodic_table[symbol].name

def get_atomic_mass(symbol):
    """Return the atomic mass of an element."""
    return periodic_table[symbol].atomic_mass


class FormulaError(ValueError):
    pass

def parse_formula(formula):
    """Convert a chemical formula for a molecule into a dictionary that
    stores the number of atoms of each element in the molecule. For
    example, this function will convert "H2O" to {"H":2, "O":1} and
    "PO4H2(CH2)12CH3" to {"P":1, "O":4, "H":29, "C":13}
    """
    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elems, symbol):
        return 0 if symbol not in elems else elems[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elems = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group, index = parse_r(formula, index + 1, level + 1)
                quant, index = parse_quant(formula, index)
                for symbol in group:
                    prev = get_quant(elems, symbol)
                    elems[symbol] = prev + group[symbol] * quant
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table:
                        index += 1
                    else:
                        # Unknown symbol for an element
                        raise FormulaError("invalid formula:", formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elems, symbol)
                elems[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    # Mismatched close parenthesis
                    raise FormulaError("invalid formula:", formula, index)
                level -= 1
                index += 1
                break
            else:
                # Illegal character: [^()0-9a-zA-Z] or decimal digit not
                # preceded by an element symbol or close parenthesis
                raise FormulaError("invalid formula:", formula, index)
        if level > 0 and level >= start_level:
            # Mismatched open parenthesis
            raise FormulaError("invalid formula:", formula, start_index - 1)
        return elems, index

    elems, _ = parse_r(formula, 0, 0)
    return elems


def molar_mass(elem_dict):
    """Compute and return the total molar mass of all
    the elements listed in elem_dict. Each item in
    elem_dict is a tuple in the form: (symbol, quantity).

    As an example, if elem_dict is {"H":2, "O":1},
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # TODO: Write this function.
    pass
