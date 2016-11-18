#!/usr/bin/env python

# This function modifies the lattice.IN file to add a fixed boundary with an inner thermal boundary.

# Note:  This script deletes the existing file and adds the selected boundary condition.

# This adds a fixed and thermal boundary
# Usage:
#
# md_setup_fixed_and_thermal_bounds.py  fixed_bound thermal_bound
#  fixed_bound must be a positive number or zero.
#  thermal_bound must be a positive number or zero.
#  if zero is passed, then the boundaries are set to free.

import os
import sys

def md_setup_fixed_and_thermal_bounds(fixed_bound,thermal_bound):
    # check the passed values are valid
    try:
        fixed_bound = float(fixed_bound)
        if( fixed_bound < 0 ):
            print("> ERROR:  The fixed boundary must be a positive number, or zero")
            print("> Exiting ...")
            sys.exit()
    except ValueError:
        print("> ERROR:  The fixed boundary must be a positive number, or zero")
        print("> Exiting ...")
        sys.exit()
    try:
        thermal_bound = float(thermal_bound)
        if( thermal_bound < 0 ):
            print("> ERROR:  The thermal boundary must be a positive number, or zero")
            print("> Exiting ...")
            sys.exit()
    except ValueError:
        print("> ERROR:  The thermal boundary must be a positive number, or zero")
        print("> Exiting ...")
        sys.exit()
    
    
    
    print(fixed_bound)
    print(thermal_bound)

        
    # if both zero is passed, generate the default lattice.IN file with free bounds
    if( (fixed_bound == 0.0) and (thermal_bound == 0.0) ):
        # remove existing file if present.
        if (os.path.isfile("lattice.IN")):
            os.remove('lattice.IN')
        # Generate file default file
        outfile = open('lattice.IN', 'w')
        outfile.write("0\n")
        outfile.write("0\n")
        outfile.write("0\n")
        outfile.write("\n")
        outfile.write("\n")
        outfile.write("2\n")
        outfile.write("    FX  0   5\n")
        outfile.write("    FX  5   0\n")
        outfile.write("2\n")
        outfile.write("    FX  0   5\n")
        outfile.write("    FX  5   0\n")
        outfile.write("2\n")
        outfile.write("    FX  0   5\n")
        outfile.write("    FX  5   0\n")
        outfile.write("\n")
        outfile.write("\n")
        outfile.write("    2                 \*NUMBER OF CONSTRAINS ALONG X DIRECTION\n")
        outfile.write("    TH  0  10\n")
        outfile.write("    TH  10  0\n")
        outfile.write("\n")
        outfile.write("    2                 \*NUMBER OF CONSTRAINS ALONG Y DIRECTION\n")
        outfile.write("    TH  0  10\n")
        outfile.write("    TH  10  0\n")
        outfile.write("\n")
        outfile.write("    2                 \*NUMBER OF CONSTRAINS ALONG Z DIRECTION\n")
        outfile.write("    TH  0  10\n")
        outfile.write("    TH  10  0\n")
        outfile.close()
    elif( (fixed_bound == 0.0) ): # only thermal bound is non zero
        # remove existing file if present.
        if (os.path.isfile("lattice.IN")):
            os.remove('lattice.IN')
        # Generate file (thermal bound)
        outfile = open('lattice.IN', 'w')
        for i in range(3):
            outfile.write("2\n")
            outfile.write("    TH  0    " + str(thermal_bound) + "\n")
            outfile.write("    TH  " + str(thermal_bound) + "  0\n")
        outfile.write("\n")
        outfile.close()
    elif( (thermal_bound == 0.0) ): # only fixed bound is non zero
        # remove existing file if present.
        if (os.path.isfile("lattice.IN")):
            os.remove('lattice.IN')
        # Generate file (fixed bound)
        outfile = open('lattice.IN', 'w')
        for i in range(3):
            outfile.write("2\n")
            outfile.write("    FX  0    " + str(fixed_bound) + "\n")
            outfile.write("    FX  " + str(fixed_bound) + "  0\n")
        outfile.write("\n")
        outfile.close()
    else:  # both fixed and thermal bound is non-zero
        # remove existing file if present.
        if (os.path.isfile("lattice.IN")):
            os.remove('lattice.IN')
        # Generate file
        outfile = open('lattice.IN', 'w')
        for i in range(3):
            outfile.write("4\n")
            outfile.write("    FX  0    " + str(fixed_bound) + "\n")
            outfile.write("    FX  " + str(fixed_bound) + "  0\n")
            outfile.write("    TH  " + str(fixed_bound) + "  " + str(fixed_bound+thermal_bound) + "\n")
            outfile.write("    TH  " + str(thermal_bound+fixed_bound) + "  " + str(fixed_bound) + "\n")
        outfile.write("\n")
        outfile.close()


if __name__ == '__main__':
    
    if (len(sys.argv) != 3):
        print("\n> The size of the fixed and thermal boundary must be given on the command-line.")
        print("> Exiting...")
        sys.exit()
    
    # Parse the fixed_bound
    fixed_bound = sys.argv[1]
    thermal_bound = sys.argv[2]
    # ensure we are given a valid number.
    try:
        fixed_bound = float(fixed_bound)
        if( fixed_bound < 0 ):
            print("> ERROR:  The fixed boundary must be a positive number, or zero")
            print("> Exiting ...")
            sys.exit()
    except ValueError:
        print("> ERROR:  The fixed boundary must be a positive number, or zero")
        print("> Exiting ...")
        sys.exit()
    try:
        thermal_bound = float(thermal_bound)
        if( thermal_bound < 0 ):
            print("> ERROR:  The thermal boundary must be a positive number, or zero")
            print("> Exiting ...")
            sys.exit()
    except ValueError:
        print("> ERROR:  The thermal boundary must be a positive number, or zero")
        print("> Exiting ...")
        sys.exit()

    md_setup_fixed_and_thermal_bounds(fixed_bound,thermal_bound)
