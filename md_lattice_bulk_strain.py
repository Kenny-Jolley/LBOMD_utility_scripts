#!/usr/bin/env python

# This function reads a lattice file and applies a uniform strain in all directions

# The function must be passed the name of the lattice file and the strain (where 1% strain is 1.01 etc)

# Kenny Jolley   Nov 2016  python 2/3

import sys
import os

def md_lattice_bulk_strain(filename,strain):

    print("> Reading file: " + str(filename) )
    if not (os.path.isfile(filename)):
        print("> Error, a required file is not present")
        print(">  " + str(filename) + " not found ...")
        sys.exit()
    
    try:
        float(strain)
    except ValueError:
        print("> Error, strain passed was not a number.")
        sys.exit()

    # Output file
    output_filename = "lattice_strained_" + str(strain) + ".dat"
    print(output_filename)

    # open files
    file = open(filename, 'r')
    outputfile = open(output_filename, 'w')

    # get num atoms
    line = file.readline()
    line = line.split()
    atoms = int(line[0])
    # write atom num to output
    outputfile.write(str(atoms) + " \n")

    # read boxsize
    line = file.readline()
    line = line.split()
    # calc strained size
    xdir = float(line[0]) * strain
    ydir = float(line[1]) * strain
    zdir = float(line[2]) * strain
    # write boxsize to output
    outputfile.write(str(xdir) + "   " + str(ydir) + "   " + str(zdir) + "\n")

    # read atom data from input, and write strained positions to output file
    while 1:
        line = file.readline()
        if not line: break
        # extract each value
        data = line.split()
        # calc strained positions
        xval = float(data[1]) * strain
        yval = float(data[2]) * strain
        zval = float(data[3]) * strain
        # write strained positions to output
        outputfile.write(data[0] + "   " +
                         str(xval) + "   " +
                         str(yval) + "   " +
                         str(zval) + "   " +
                         data[4] + " \n")

    file.close()
    outputfile.close()





if __name__ == '__main__':
    print("\nThis script reads a lattice file and applies a uniform strain in all directions\n")
    if len(sys.argv) == 3:
        file = str(sys.argv[1])
        try:
            strain = float(sys.argv[2])
        except ValueError:
            print("> Error, strain passed was not a number.")
            print(" Value given: " + str(sys.argv[2]) )
            sys.exit()
    else:
        print("> command-line usage:")
        print("> md_lattice_bulk_strain.py  filename strain ")
        sys.exit()

    md_lattice_bulk_strain(file,strain)


sys.exit()


