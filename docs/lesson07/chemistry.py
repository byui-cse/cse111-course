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
    table = {
        "H"  : Element("Hydrogen", "H", 1.01),
        "He" : Element("Helium", "He", 4.002602),
        "Li" : Element("Lithium", "Li", 6.941),
        "Be" : Element("Beryllium", "Be", 9.012182),
        "B"  : Element("Boron", "B", 10.811),
        "C"  : Element("Carbon", "C", 12.01),
        "N"  : Element("Nitrogen", "N", 14.0067),
        "O"  : Element("Oxygen", "O", 15.9994),
        "F"  : Element("Fluorine", "F", 18.9984032),
        "Ne" : Element("Neon", "Ne", 20.1797),
        "Na" : Element("Sodium", "Na", 22.98976928),
        "Mg" : Element("Magnesium", "Mg", 24.305),
        "Al" : Element("Aluminium", "Al", 26.9815386),
        "Si" : Element("Silicon", "Si", 28.0855),
        "P"  : Element("Phosphorus", "P", 30.973762),
        "S"  : Element("Sulfur", "S", 32.065),
        "Cl" : Element("Chlorine", "Cl", 35.453),
        "Ar" : Element("Argon", "Ar", 39.948),
        "K"  : Element("Potassium", "K", 39.0983),
        "Ca" : Element("Calsium", "Ca", 40.078),
        "Sc" : Element("Scandium", "Sc", 44.955912),
        "Ti" : Element("Titanium", "Ti", 47.9),
        "V"  : Element("Vanadium", "V", 50.9415),
        "Cr" : Element("Chromium", "Cr", 51.9961),
        "Mn" : Element("Manganese", "Mn", 54.938045),
        "Fe" : Element("Iron", "Fe", 55.845),
        "Co" : Element("Cobalt", "Co", 58.933195),
        "Ni" : Element("Nickel", "Ni", 58.6934),
        "Cu" : Element("Copper", "Cu", 63.546),
        "Zn" : Element("Zinc", "Zn", 65.38),
        "Ga" : Element("Gallium", "Ga", 69.723),
        "Ge" : Element("Germanium", "Ge", 72.64),
        "As" : Element("Arsenic", "As", 74.9216),
        "Se" : Element("Selenium", "Se", 78.96),
        "Br" : Element("Bromine", "Br", 79.904),
        "Kr" : Element("Krypton", "Kr", 83.798),
        "Rb" : Element("Rubidium", "Rb", 85.4678),
        "Sr" : Element("Strontium", "Sr", 87.62),
        "Y"  : Element("Yttrium", "Y", 88.90585),
        "Zr" : Element("Zirconium", "Zr", 91.224),
        "Nb" : Element("Niobium", "Nb", 92.90638),
        "Mo" : Element("Molybdenum", "Mo", 95.96),
        "Tc" : Element("Technetium", "Tc", 98),
        "Ru" : Element("Ruthenium", "Ru", 101.07),
        "Rh" : Element("Rhodium", "Rh", 102.9055),
        "Pd" : Element("Palladium", "Pd", 106.42),
        "Ag" : Element("Silver", "Ag", 107.8682),
        "Cd" : Element("Cadmium", "Cd", 112.411),
        "In" : Element("Indium", "In", 114.818),
        "Sn" : Element("Tin", "Sn", 118.71),
        "Sb" : Element("Antimony", "Sb", 121.76),
        "Te" : Element("Tellurium", "Te", 127.6),
        "I"  : Element("Iodine", "I", 126.90447),
        "Xe" : Element("Xenon", "Xe", 131.293),
        "Cs" : Element("Cesium", "Cs", 132.9054519),
        "Ba" : Element("Barium", "Ba", 137.327),
        "La" : Element("Lanthanum", "La", 138.90547),
        "Ce" : Element("Cerium", "Ce", 140.116),
        "Pr" : Element("Crazyname", "Pr", 140.90765),
        "Nd" : Element("Neodymium", "Nd", 144.242),
        "Pm" : Element("Promethium", "Pm", 145),
        "Sm" : Element("Samarium", "Sm", 150.36),
        "Eu" : Element("Europium", "Eu", 151.964),
        "Gd" : Element("Gadolinium", "Gd", 157.25),
        "Tb" : Element("Terbium", "Tb", 158.92535),
        "Dy" : Element("Dysprosium", "Dy", 162.5),
        "Ho" : Element("Holmium", "Ho", 164.93032),
        "Er" : Element("Erbium", "Er", 167.259),
        "Tm" : Element("Thulium", "Tm", 168.93421),
        "Yb" : Element("Ytterbium", "Yb", 173.054),
        "Lu" : Element("Lutetium", "Lu", 174.9668),
        "Hf" : Element("Hafnium", "Hf", 178.49),
        "Ta" : Element("Tantalum", "Ta", 180.94788),
        "W"  : Element("Tungsten", "W", 183.84),
        "Re" : Element("Rhenium", "Re", 186.207),
        "Os" : Element("Osmium", "Os", 190.23),
        "Ir" : Element("Iridium", "Ir", 192.217),
        "Pt" : Element("Platinum", "Pt", 195.084),
        "Au" : Element("Gold", "Au", 196.966569),
        "Hg" : Element("Mercury", "Hg", 200.59),
        "Tl" : Element("Thallium", "Tl", 204.3833),
        "Pb" : Element("Lead", "Pb", 207.2),
        "Bi" : Element("Bismuth", "Bi", 208.9804),
        "Po" : Element("Polonium", "Po", 209),
        "At" : Element("Astatine", "At", 210),
        "Rn" : Element("Radon", "Rn", 222),
        "Fr" : Element("Francium", "Fr", 223),
        "Ra" : Element("Radium", "Ra", 226),
        "Ac" : Element("Actinium", "Ac", 227),
        "Th" : Element("Thorium", "Th", 232.03806),
        "Pa" : Element("Whonamedthis", "Pa", 231.03588),
        "U"  : Element("Uranium", "U", 238.02891),
        "Np" : Element("Neptunium", "Np", 237),
        "Pu" : Element("Plutonium", "Pu", 244),
        "Am" : Element("Americium", "Am", 243),
        "Cm" : Element("Curium", "Cm", 247),
        "Bk" : Element("Berkelium", "Bk", 247),
        "Cf" : Element("Californium", "Cf", 251),
        "Es" : Element("Einsteinium", "Es", 252),
        "Fm" : Element("Fermium", "Fm", 257),
        "Md" : Element("Mendelevium", "Md", 258),
        "No" : Element("Nobelium", "No", 259),
        "Lr" : Element("Lawrencium", "Lr", 262),
        "Rf" : Element("Rutherfordium", "Rf", 267),
        "Db" : Element("Dubnium", "Db", 268),
        "Sg" : Element("Seaborgium", "Sg", 271),
        "Bh" : Element("Bohrium", "Bh", 272),
        "Hs" : Element("Hassium", "Hs", 270),
        "Mt" : Element("Meitnerium", "Mt", 276),
        "Ds" : Element("Darmstadtium", "Ds", 281),
        "Rg" : Element("Roentgenium", "Rg", 280),
        "Cn" : Element("Copernicium", "Cn", 285),
        "Nh" : Element("Nihonium", "Nh", 284),
        "Fl" : Element("Flerovium", "Fl", 289),
        "Mc" : Element("Moscovium", "Mc", 288),
        "Lv" : Element("Livermorium", "Lv", 293),
        "Ts" : Element("Tennessine", "Ts", 294),
        "Og" : Element("Oganesson", "Og", 294)
    }
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
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """
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
        elems = {}  # A dictionary that holds symbol quantity pairs
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


def molar_mass(symbol_quantity_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_dict. Each item in
    symbol_quantity_dict is a tuple in the form: (symbol, quantity).

    As an example, if symbol_quantity_dict is {"H":2, "O":1},
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    total_mass = 0

    # For each item in the dictionary:
    #   Split the item into symbol and quantity (key and value).
    #   Get the atomic mass for the symbol.
    #   Multiply the atomic mass by the quantity.
    #   Add the product into the total mass.
    for symbol, quantity in symbol_quantity_dict.items():
        atomic_mass = get_atomic_mass(symbol)
        total_mass += atomic_mass * quantity

    # Return the total mass.
    return total_mass
