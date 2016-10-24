# md_constants.py
# use ->  from md_constants import *
#  to access variable directly
#  OR
# use ->  import md_constants
#  Then access values like this: md_constants.amu  (for amu parameter for example).

# A library of pysical and mathematical constants
# kenny Jolley, Jun 2013

# Maths
pi = 3.14159265358979323846
e =  2.71828182845904523536


# Pysics
e0  = 8.854187817E-12       # electric constant \epsilion _0  in [F m-1]
Z0  = 376.730313461         # characteristic impedance of vacuum [\Omega]
m0  = 4*pi*1E-7             # magnetic constant  [N A-2] 
G   = 6.67384E-11           # Newtonian constant of gravitation [m3 kg-1 s-2]
h   = 6.62606957E-34        # Planck constant [J s]
hbar= h/(2.0*pi)            # Planck constant over 2 pi [J s]
lp  = 1.616199E-35          # Planck length [m]
mp  = 2.17651E-8            # Planck mass [kg]
Tp  = 1.416833E+32          # Planck temperature [K]
tp  = 5.39106E-44           # Planck time [s]
c   = 299792458             # speed of light in vacuum [m s-1]

amu = 1.660538921E-27       # in kg
amu_evc2 = 931.494061E+6    # in eV/c^2
me  = 9.10938291E-31        # electron mass [kg]
eV  = 1.602176565E-19       # electron volt [J]
F   = 96485.3365            # Faraday constant [C mol-1]
R   = 8.3144621             # molar gas constant [J mol-1 K-1]
a   = 7.2973525698E-3       # fine-structure constant
NA  = 6.02214129E+23        # Avogadro constant [mol-1]
k   = 1.3806488E-23         # Boltzmann constant  [J K-1]
kb  = k                     # Boltzmann constant  [J K-1]
Rinf= 10973731.568539       # Rydberg constant  [m-1]


# Conversions  - multiply value by conversion factor to compute result
deg2rad = pi/180            # degrees to radians
rad2deg = 180/pi            # radians to degrees
# -length
inch2m  = 0.0254
inch2cm = 2.54
inch2mm = 25.4
m2inch  = (1.0/0.0254)
cm2inch = (1.0/2.54)
mm2inch = (1.0/25.4)
inch2foot = 1.0/12.0
foot2inch = 12.0

#    ! Setup atomic array with atom data
#    ! Atomic symbols
atomic_symbol = ["HH" for x in range(114)]
atomic_symbol[0] = "ZZ"
atomic_symbol[1] = "H_"
atomic_symbol[2] = "He"
atomic_symbol[3] = "Li"
atomic_symbol[4] = "Be"
atomic_symbol[5] = "B_"
atomic_symbol[6] = "C_"
atomic_symbol[7] = "N_"
atomic_symbol[8] = "O_"
atomic_symbol[9] = "F_"
atomic_symbol[10] = "Ne"
atomic_symbol[11] = "Na"
atomic_symbol[12] = "Mg"
atomic_symbol[13] = "Al"
atomic_symbol[14] = "Si"
atomic_symbol[15] = "P_"
atomic_symbol[16] = "S_"
atomic_symbol[17] = "Cl"
atomic_symbol[18] = "Ar"
atomic_symbol[19] = "K_"
atomic_symbol[20] = "Ca"
atomic_symbol[21] = "Sc"
atomic_symbol[22] = "Ti"
atomic_symbol[23] = "V_"
atomic_symbol[24] = "Cr"
atomic_symbol[25] = "Mn"
atomic_symbol[26] = "Fe"
atomic_symbol[27] = "Co"
atomic_symbol[28] = "Ni"
atomic_symbol[29] = "Cu"
atomic_symbol[30] = "Zn"
atomic_symbol[31] = "Ga"
atomic_symbol[32] = "Ge"
atomic_symbol[33] = "As"
atomic_symbol[34] = "Se"
atomic_symbol[35] = "Br"
atomic_symbol[36] = "Kr"
atomic_symbol[37] = "Rb"
atomic_symbol[38] = "Sr"
atomic_symbol[39] = "Y_"
atomic_symbol[40] = "Zr"
atomic_symbol[41] = "Nb"
atomic_symbol[42] = "Mo"
atomic_symbol[43] = "Tc"
atomic_symbol[44] = "Ru"
atomic_symbol[45] = "Rh"
atomic_symbol[46] = "Pd"
atomic_symbol[47] = "Ag"
atomic_symbol[48] = "Cd"
atomic_symbol[49] = "In"
atomic_symbol[50] = "Sn"
atomic_symbol[51] = "Sb"
atomic_symbol[52] = "Te"
atomic_symbol[53] = "I_"
atomic_symbol[54] = "Xe"
atomic_symbol[55] = "Cs"
atomic_symbol[56] = "Ba"
atomic_symbol[57] = "La"
atomic_symbol[58] = "Ce"
atomic_symbol[59] = "Pr"
atomic_symbol[60] = "Nd"
atomic_symbol[61] = "Pm"
atomic_symbol[62] = "Sm"
atomic_symbol[63] = "Eu"
atomic_symbol[64] = "Gd"
atomic_symbol[65] = "Tb"
atomic_symbol[66] = "Dy"
atomic_symbol[67] = "Ho"
atomic_symbol[68] = "Er"
atomic_symbol[69] = "Tm"
atomic_symbol[70] = "Yb"
atomic_symbol[71] = "Lu"
atomic_symbol[72] = "Hf"
atomic_symbol[73] = "Ta"
atomic_symbol[74] = "W_"
atomic_symbol[75] = "Re"
atomic_symbol[76] = "Os"
atomic_symbol[77] = "Ir"
atomic_symbol[78] = "Pt"
atomic_symbol[79] = "Au"
atomic_symbol[80] = "Hg"
atomic_symbol[81] = "Tl"
atomic_symbol[82] = "Pb"
atomic_symbol[83] = "Bi"
atomic_symbol[84] = "Po"
atomic_symbol[85] = "At"
atomic_symbol[86] = "Rn"
atomic_symbol[87] = "Fr"
atomic_symbol[88] = "Ra"
atomic_symbol[89] = "Ac"
atomic_symbol[90] = "Th"
atomic_symbol[91] = "Pa"
atomic_symbol[92] = "U_"
atomic_symbol[93] = "Np"
atomic_symbol[94] = "Pu"
atomic_symbol[95] = "Am"
atomic_symbol[96] = "Cm"
atomic_symbol[97] = "Bk"
atomic_symbol[98] = "Cf"
atomic_symbol[99] = "Es"
atomic_symbol[100] = "Fm"
atomic_symbol[101] = "Md"
atomic_symbol[102] = "No"
atomic_symbol[103] = "Lr"
atomic_symbol[104] = "Rf"
atomic_symbol[105] = "Db"
atomic_symbol[106] = "Sg"
atomic_symbol[107] = "Bh"
atomic_symbol[108] = "Hs"
atomic_symbol[109] = "Mt"
atomic_symbol[110] = "Ds"
atomic_symbol[111] = "Rg"
atomic_symbol[112] = "Cn"
atomic_symbol[113] = "FF"  # needed for Fe3+ symbol

#    ! Atomic names (British spelling)
atomic_name = ["HH" for x in range(114)]
atomic_name[0] = "ZZ"
atomic_name[1] = "Hydrogen"
atomic_name[2] = "Helium"
atomic_name[3] = "Lithium"
atomic_name[4] = "Beryllium"
atomic_name[5] = "Boron"
atomic_name[6] = "Carbon"
atomic_name[7] = "Nitrogen"
atomic_name[8] = "Oxygen"
atomic_name[9] = "Fluorine"
atomic_name[10] = "Neon"
atomic_name[11] = "Sodium"
atomic_name[12] = "Magnesium"
atomic_name[13] = "Aluminium"
atomic_name[14] = "Silicon"
atomic_name[15] = "Phosphorus"
atomic_name[16] = "Sulphur"
atomic_name[17] = "Chlorine"
atomic_name[18] = "Argon"
atomic_name[19] = "Potassium"
atomic_name[20] = "Calcium"
atomic_name[21] = "Scandium"
atomic_name[22] = "Titanium"
atomic_name[23] = "Vanadium"
atomic_name[24] = "Chromium"
atomic_name[25] = "Manganese"
atomic_name[26] = "Iron"
atomic_name[27] = "Cobalt"
atomic_name[28] = "Nickel"
atomic_name[29] = "Copper"
atomic_name[30] = "Zinc"
atomic_name[31] = "Gallium"
atomic_name[32] = "Germanium"
atomic_name[33] = "Arsenic"
atomic_name[34] = "Selenium"
atomic_name[35] = "Bromine"
atomic_name[36] = "Krypton"
atomic_name[37] = "Rubidium"
atomic_name[38] = "Strontium"
atomic_name[39] = "Yttrium"
atomic_name[40] = "Zirconium"
atomic_name[41] = "Niobium"
atomic_name[42] = "Molybdenum"
atomic_name[43] = "Technetium"
atomic_name[44] = "Ruthenium"
atomic_name[45] = "Rhodium"
atomic_name[46] = "Palladium"
atomic_name[47] = "Silver"
atomic_name[48] = "Cadmium"
atomic_name[49] = "Indium"
atomic_name[50] = "Tin"
atomic_name[51] = "Antimony"
atomic_name[52] = "Tellurium"
atomic_name[53] = "Iodine"
atomic_name[54] = "Xenon"
atomic_name[55] = "Caesium"
atomic_name[56] = "Barium"
atomic_name[57] = "Lanthanum"
atomic_name[58] = "Cerium"
atomic_name[59] = "Praseodymium"
atomic_name[60] = "Neodymium"
atomic_name[61] = "Promethium"
atomic_name[62] = "Samarium"
atomic_name[63] = "Europium"
atomic_name[64] = "Gadolinium"
atomic_name[65] = "Terbium"
atomic_name[66] = "Dysprosium"
atomic_name[67] = "Holmium"
atomic_name[68] = "Erbium"
atomic_name[69] = "Thulium"
atomic_name[70] = "Ytterbium"
atomic_name[71] = "Lutetium"
atomic_name[72] = "Hafnium"
atomic_name[73] = "Tantalum"
atomic_name[74] = "Tungsten"
atomic_name[75] = "Rhenium"
atomic_name[76] = "Osmium"
atomic_name[77] = "Iridium"
atomic_name[78] = "Platinum"
atomic_name[79] = "Gold"
atomic_name[80] = "Mercury"
atomic_name[81] = "Thallium"
atomic_name[82] = "Lead"
atomic_name[83] = "Bismuth"
atomic_name[84] = "Polonium"
atomic_name[85] = "Astatine"
atomic_name[86] = "Radon"
atomic_name[87] = "Francium"
atomic_name[88] = "Radium"
atomic_name[89] = "Actinium"
atomic_name[90] = "Thorium"
atomic_name[91] = "Protactinium"
atomic_name[92] = "Uranium"
atomic_name[93] = "Neptunium"
atomic_name[94] = "Plutonium"
atomic_name[95] = "Americium"
atomic_name[96] = "Curium"
atomic_name[97] = "Berkelium"
atomic_name[98] = "Californium"
atomic_name[99] = "Einsteinium"
atomic_name[100] = "Fermium"
atomic_name[101] = "Mendelevium"
atomic_name[102] = "Nobelium"
atomic_name[103] = "Lawrencium"
atomic_name[104] = "Rutherfordium"
atomic_name[105] = "Dubnium"
atomic_name[106] = "Seaborgium"
atomic_name[107] = "Bohrium"
atomic_name[108] = "Hassium"
atomic_name[109] = "Meitnerium"
atomic_name[110] = "Darmstadtium"
atomic_name[111] = "Roentgenium"
atomic_name[112] = "Copernicium"
atomic_name[113] = "Iron 3+"      # ! Additional label for Fe3+ ions used in simulations elsewhere


#    Atomic masses  in amu
atomic_mass= [0.0 for x in range(114)]
#    atomic mass (in AMU) of an element from Wikipedia (http://en.wikipedia.org/wiki/)
atomic_mass[0]   = 0.000            # ZERO
atomic_mass[1]   = 1.008            # H_    ! Wiki
atomic_mass[2]   = 4.002602         # He    ! Wiki
atomic_mass[3]   = 6.94             # Li    ! Wiki
atomic_mass[4]   = 9.012182         # Be    ! Wiki
atomic_mass[5]   = 10.81            # B_    ! Wiki
atomic_mass[6]   = 12.011           # C_    ! Wiki
atomic_mass[7]   = 14.007           # N_    ! Wiki
atomic_mass[8]   = 15.9994          # O_    ! Wiki
atomic_mass[9]   = 18.998403163     # F_    ! Wiki
atomic_mass[10]  = 20.1797          # Ne    ! Wiki
atomic_mass[11]  = 22.98976928      # Na    ! Wiki
atomic_mass[12]  = 24.305           # Mg    ! Wiki
atomic_mass[13]  = 26.98153857      # Al    ! Wiki
atomic_mass[14]  = 28.0851          # Si    ! Wiki
atomic_mass[15]  = 30.973761998     # P_    ! Wiki
atomic_mass[16]  = 32.066           # S_    ! Wiki
atomic_mass[17]  = 35.45            # Cl    ! Wiki
atomic_mass[18]  = 39.948           # Ar    ! Wiki
atomic_mass[19]  = 39.0983          # K_    ! Wiki
atomic_mass[20]  = 40.078           # Ca    ! Wiki
atomic_mass[21]  = 44.955908        # Sc    ! Wiki
atomic_mass[22]  = 47.867           # Ti    ! Wiki
atomic_mass[23]  = 50.9415          # V_    ! Wiki
atomic_mass[24]  = 51.9961          # Cr    ! Wiki
atomic_mass[25]  = 54.938044        # Mn    ! Wiki
atomic_mass[26]  = 55.845           # Fe    ! Wiki
atomic_mass[27]  = 58.933194        # Co    ! Wiki
atomic_mass[28]  = 58.6934          # Ni    ! Wiki
atomic_mass[29]  = 63.546           # Cu    ! Wiki
atomic_mass[30]  = 65.38            # Zn    ! Wiki
atomic_mass[31]  = 69.723           # Ga    ! Wiki
atomic_mass[32]  = 72.63            # Ge    ! Wiki
atomic_mass[33]  = 74.921595        # As    ! Wiki
atomic_mass[34]  = 78.971           # Se    ! Wiki
atomic_mass[35]  = 79.904           # Br    ! Wiki
atomic_mass[36]  = 83.798           # Kr    ! Wiki
atomic_mass[37]  = 85.4678          # Rb    ! Wiki
atomic_mass[38]  = 87.62            # Sr    ! Wiki
atomic_mass[39]  = 88.90584         # Y_    ! Wiki
atomic_mass[40]  = 91.224           # Zr    ! Wiki
atomic_mass[41]  = 92.90637         # Nb    ! Wiki
atomic_mass[42]  = 95.95            # Mo    ! Wiki
atomic_mass[43]  = 98.0             # Tc    ! Wiki
atomic_mass[44]  = 101.07           # Ru    ! Wiki
atomic_mass[45]  = 102.9055         # Rh    ! Wiki
atomic_mass[46]  = 106.42           # Pd    ! Wiki
atomic_mass[47]  = 107.8682         # Ag    ! Wiki
atomic_mass[48]  = 112.414          # Cd    ! Wiki
atomic_mass[49]  = 114.818          # In    ! Wiki
atomic_mass[50]  = 118.710          # Sn    ! Wiki
atomic_mass[51]  = 121.760          # Sb    ! Wiki  http://en.wikipedia.org/wiki/Antimony
atomic_mass[52]  = 127.60           # Te    ! Wiki  http://en.wikipedia.org/wiki/Tellurium
atomic_mass[53]  = 126.90447        # I_    ! Wiki  http://en.wikipedia.org/wiki/Iodine
atomic_mass[54]  = 131.293          # Xe    ! Wiki  http://en.wikipedia.org/wiki/Xenon
atomic_mass[55]  = 132.90545196     # Cs    ! Wiki  http://en.wikipedia.org/wiki/Caesium
atomic_mass[56]  = 137.327          # Ba    ! Wiki  http://en.wikipedia.org/wiki/Barium
atomic_mass[57]  = 138.90547        # La    ! Wiki  http://en.wikipedia.org/wiki/Lanthanum
atomic_mass[58]  = 140.116          # Ce    ! Wiki  http://en.wikipedia.org/wiki/Cerium
atomic_mass[59]  = 140.90766        # Pr    ! Wiki  http://en.wikipedia.org/wiki/Praseodymium
atomic_mass[60]  = 144.242          # Nd    ! Wiki  http://en.wikipedia.org/wiki/Neodymium
atomic_mass[61]  = 145.0            # Pm    ! Wiki  http://en.wikipedia.org/wiki/Promethium
atomic_mass[62]  = 150.36           # Sm    ! Wiki  http://en.wikipedia.org/wiki/Samarium
atomic_mass[63]  = 151.964          # Eu    ! Wiki  http://en.wikipedia.org/wiki/Europium
atomic_mass[64]  = 157.25           # Gd    ! Wiki  http://en.wikipedia.org/wiki/Gadolinium
atomic_mass[65]  = 158.92535        # Tb    ! Wiki  http://en.wikipedia.org/wiki/Terbium
atomic_mass[66]  = 162.5            # Dy    ! Wiki  http://en.wikipedia.org/wiki/Dysprosium
atomic_mass[67]  = 164.93033        # Ho    ! Wiki  http://en.wikipedia.org/wiki/Holmium
atomic_mass[68]  = 167.259          # Er    ! Wiki  http://en.wikipedia.org/wiki/Erbium
atomic_mass[69]  = 168.93422        # Tm    ! Wiki  http://en.wikipedia.org/wiki/Thulium
atomic_mass[70]  = 173.054          # Yb    ! Wiki  http://en.wikipedia.org/wiki/Ytterbium
atomic_mass[71]  = 174.9668         # Lu    ! Wiki  http://en.wikipedia.org/wiki/Lutetium
atomic_mass[72]  = 178.49           # Hf    ! Wiki  http://en.wikipedia.org/wiki/Hafnium
atomic_mass[73]  = 180.94788        # Ta    ! Wiki  http://en.wikipedia.org/wiki/Tantalum
atomic_mass[74]  = 183.84           # W_    ! Wiki  http://en.wikipedia.org/wiki/Tungsten
atomic_mass[75]  = 186.207          # Re    ! Wiki  http://en.wikipedia.org/wiki/Rhenium
atomic_mass[76]  = 190.23           # Os    ! Wiki  http://en.wikipedia.org/wiki/Osmium
atomic_mass[77]  = 192.217          # Ir    ! Wiki  http://en.wikipedia.org/wiki/Iridium
atomic_mass[78]  = 195.084          # Pt    ! Wiki  http://en.wikipedia.org/wiki/Platinum
atomic_mass[79]  = 196.966569       # Au    ! Wiki  http://en.wikipedia.org/wiki/Gold
atomic_mass[80]  = 200.592          # Hg    ! Wiki  http://en.wikipedia.org/wiki/Mercury_%28element%29
atomic_mass[81]  = 204.38           # Tl    ! Wiki  http://en.wikipedia.org/wiki/Thallium
atomic_mass[82]  = 207.2            # Pb    ! Wiki  http://en.wikipedia.org/wiki/Lead
atomic_mass[83]  = 208.98040        # Bi    ! Wiki  http://en.wikipedia.org/wiki/Bismuth
atomic_mass[84]  = 209.0            # Po    ! Wiki  http://en.wikipedia.org/wiki/Polonium
atomic_mass[85]  = 210.0            # At    ! Wiki  http://en.wikipedia.org/wiki/Astatine
atomic_mass[86]  = 222.0            # Rn    ! Wiki  http://en.wikipedia.org/wiki/Radon
atomic_mass[87]  = 223.0            # Fr    ! Wiki  http://en.wikipedia.org/wiki/Francium
atomic_mass[88]  = 226.0            # Ra    ! Wiki  http://en.wikipedia.org/wiki/Radium
atomic_mass[89]  = 227.0            # Ac    ! Wiki  http://en.wikipedia.org/wiki/Actinium
atomic_mass[90]  = 232.0377         # Th    ! Wiki  http://en.wikipedia.org/wiki/Thorium
atomic_mass[91]  = 231.03588        # Pa    ! Wiki  http://en.wikipedia.org/wiki/Protactinium
atomic_mass[92]  = 238.02891        # U_    ! Wiki  http://en.wikipedia.org/wiki/Uranium
atomic_mass[93]  = 237.0            # Np    ! Wiki  http://en.wikipedia.org/wiki/Neptunium
atomic_mass[94]  = 244.0            # Pu    ! Wiki  http://en.wikipedia.org/wiki/Plutonium
atomic_mass[95]  = 243.0            # Am    ! Wiki  http://en.wikipedia.org/wiki/Americium
atomic_mass[96]  = 247.0            # Cm    ! Wiki  http://en.wikipedia.org/wiki/Curium
atomic_mass[97]  = 247.0            # Bk    ! Wiki  http://en.wikipedia.org/wiki/Berkelium
atomic_mass[98]  = 251.0            # Cf    ! Wiki  http://en.wikipedia.org/wiki/Californium
atomic_mass[99]  = 252.0            # Es    ! Wiki  http://en.wikipedia.org/wiki/Einsteinium
atomic_mass[100] = 257.0            # Fm    ! Wiki  http://en.wikipedia.org/wiki/Fermium
atomic_mass[101] = 258.0            # Md    ! Wiki  http://en.wikipedia.org/wiki/Mendelevium
atomic_mass[102] = 259.0            # No    ! Wiki  http://en.wikipedia.org/wiki/Nobelium
atomic_mass[103] = 262.0            # Lr    ! Wiki  http://en.wikipedia.org/wiki/Lawrencium
atomic_mass[104] = 267.0            # Rf    ! Wiki  http://en.wikipedia.org/wiki/Rutherfordium
atomic_mass[105] = 268.0            # Db    ! Wiki  http://en.wikipedia.org/wiki/Dubnium
atomic_mass[106] = 269.0            # Sg    ! Wiki  http://en.wikipedia.org/wiki/Seaborgium
atomic_mass[107] = 270.0            # Bh    ! Wiki  http://en.wikipedia.org/wiki/Bohrium
atomic_mass[108] = 269.0            # Hs    ! Wiki  http://en.wikipedia.org/wiki/Hassium
atomic_mass[109] = 278.0            # Mt    ! Wiki  http://en.wikipedia.org/wiki/Meitnerium
atomic_mass[110] = 281.0            # Ds    ! Wiki  http://en.wikipedia.org/wiki/Darmstadtium
atomic_mass[111] = 281.0            # Rg    ! Wiki  http://en.wikipedia.org/wiki/Roentgenium
atomic_mass[112] = 285.0            # Cn    ! Wiki  http://en.wikipedia.org/wiki/Copernicium
atomic_mass[113] = 55.845           # Fe3+    ! Wiki


def find_atomic_num(atom_name):
    for i in range(114):
        if(atom_name.lower() == atomic_symbol[i].lower()):
            return i
        if(atom_name.lower() == atomic_name[i].lower()):
            return i
        if(len(atom_name) == 1):
            if( (atom_name[0].lower() == atomic_symbol[i][0].lower()) and (atomic_symbol[i][1] == "_" )  ):
                return i
    print("Failed to find atom symbol " + str(atom_name) + " in list")
    return -1

