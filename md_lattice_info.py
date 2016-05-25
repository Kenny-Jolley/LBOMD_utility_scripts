#!/usr/bin/env python

# This function reads a lattice file and prints some basic
# information about the lattice

# Kenny Jolley   May 2016  python 2

import sys, os
import md_constants


def md_lattice_info(lattice_filename):
    # check file exists
    if (os.path.isfile(lattice_filename)):
        print("Found: " + lattice_filename)
    else:
        print(lattice_filename + " not found, exiting ...")
        return

    print("+----------------------------+")
    print("| Lattice info               |")
    print("+----------------------------+")
    # read lattice file header
    infile = open(lattice_filename, 'r')
    fileline = infile.readline()
    fileline = fileline.split()
    atoms = int(fileline[0])
    print("Atoms:     " + str(atoms))
    fileline = infile.readline()
    fileline = fileline.split()
    box_x = float(fileline[0])
    box_y = float(fileline[1])
    box_z = float(fileline[2])
    volume = box_x*box_y*box_z
    print("Cell size: " + str(box_x) + " " + str(box_y) + " " + str(box_z) + "  Angstroms")
    print("Volume:    " + str(volume) + "  Angstroms^3")

    # find number of each atom
    atomnum_list = [0 for x in xrange(114)]

    while 1:
        fileline = infile.readline()
        if not fileline: break
    
        fileline = fileline.split()
        # find atom num
        num = md_constants.find_atomic_num(str(fileline[0]))
        # increment counter
        atomnum_list[num] = atomnum_list[num] + 1
    infile.close()

    # print number of each atom type
    print("List of atoms in the system")
    for x in range(0,len(atomnum_list)):
        if(atomnum_list[x] > 0):
            print(str(md_constants.atomic_symbol[x]) + " " + str(atomnum_list[x]) )

    # Calculate the system mass and density
    total_mass = 0
    for x in range(0,len(atomnum_list)):
        total_mass = total_mass + atomnum_list[x]*md_constants.atomic_mass[x]
    print("System mass: " + str(total_mass) + " amu")
    total_mass = total_mass * md_constants.amu
    print("System mass: " + str(total_mass) + " Kg")
    density = total_mass*1e27/volume
    print("Density:     " + str(density) + " g/cm^3")


if __name__ == '__main__':
    print("\nThis function reads a lattice file and prints")
    print("some basic information about the lattice.\n")
    if len(sys.argv) == 2:
        filename = str(sys.argv[1])
        print("Reading file:  " + filename)
    else:
        print("You must enter a lattice filename to read.")
        filename = raw_input('Enter filename: ')
        filename = str(filename)
        print("Reading file:  " + filename)
    md_lattice_info(filename)


