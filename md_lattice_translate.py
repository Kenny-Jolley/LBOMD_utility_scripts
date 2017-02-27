#!/usr/bin/env python

# This function reads the lattice.dat file and translates the atoms by a user specified amount

# The user selects the translation in each direction in Angstroms, either on
# the command-line, or interactively.

# Kenny Jolley   Feb 2017  python 2/3

import sys

def md_lattice_translate(x,y,z):
    # Input file
    file = open('lattice.dat', 'r')
    # Output file
    output_filename = "lattice_translated_" + str(x) + "_" + str(y) + "_"+ str(z) + ".dat"
    print(output_filename)
    outputfile = open(output_filename, 'w')

    # atoms
    line = file.readline()
    line = line.split()
    atoms = int(line[0])
    # box
    line = file.readline()
    line = line.split()
    boxx = float(line[0])
    boxy = float(line[1])
    boxz = float(line[2])
    
    # output header (this does not change)
    outputfile.write(str(atoms) + ' \n')
    outputfile.write(str(boxx) + '    ' + str(boxy) + '    ' + str(boxz) + ' \n')
    
    # read atoms from input file, and write translated coords to new file
    for i in range(1,atoms+1):
        line = file.readline()
        if not line: break
        
        data = line.split()
        
        # translate data points
        atomtype = data[0]
        xval = float(data[1]) + x
        yval = float(data[2]) + y
        zval = float(data[3]) + z
        atomcharge = float(data[4])
    
        # Wrap around periodic boundaries
        if (xval > boxx):
            xval = xval - boxx
        if (xval < 0.0):
            xval = xval + boxx
        if (yval > boxy):
            yval = yval - boxy
        if (yval < 0.0):
            yval = yval + boxy
        if (zval > boxz):
            zval = zval - boxz
        if (zval < 0.0):
            zval = zval + boxz

        # write line to new file
        outputfile.write(str(atomtype) + '    ' +
                         str(xval) + '    ' +
                         str(yval) + '    ' +
                         str(zval) + '    ' +
                         str(atomcharge) + ' \n')
    
    file.close()
    outputfile.close()


if __name__ == '__main__':
    print("\nThis script reads the lattice.dat file and ")
    print("translates the atoms by a user specified amount\n")
    if len(sys.argv) == 4:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        z = float(sys.argv[3])
        print("Translation vector:  (" + str(x) + ", " + str(y) + ", " + str(z) + ")")
    else:
        print("You must set cell no. in x, y and z")
        if sys.version_info[0] < 3:
            x = raw_input('Enter translation in x-dir: ')
            x = float(x)
            y = raw_input('Enter translation in y-dir: ')
            y = float(y)
            z = raw_input('Enter translation in z-dir: ')
            z = float(z)
        else:
            x = input('Enter translation in x-dir: ')
            x = float(x)
            y = input('Enter translation in y-dir: ')
            y = float(y)
            z = input('Enter translation in z-dir: ')
            z = float(z)
        print("Translation vector:  (" + str(x) + ", " + str(y) + ", " + str(z) + ")")
    md_lattice_translate(x,y,z)
