#!/usr/bin/env python

# This function modifies the lattice.IN file to add a fixed boundary.

# Note:  This script deletes the existing file and adds the selected fixed boundary.

# This adds a fixed boundary
# Usage:
#
# md_setup_fixed_bounds.py  fixed_bound
#  fixed_bound must be a positive number or zero.
#  if zero is passed, then the boundaries are set to free.

import os
import sys

def md_setup_fixed_bounds(fixed_bound):
    # check the passed value is valid
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
    
    
    print(fixed_bound)
        
    # if zero is passed, generate the default lattice.IN file with free bounds
    if(fixed_bound == 0.0):
        # remove existing file if present.
        if (os.path.isfile("lattice.IN")):
            os.remove('lattice.IN')
        # Generate file
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
    else:
        # remove existing file if present.
        if (os.path.isfile("lattice.IN")):
            os.remove('lattice.IN')
        # Generate file
        outfile = open('lattice.IN', 'w')
        outfile.write("2\n")
        outfile.write("    FX  0    " + str(fixed_bound) + "\n")
        outfile.write("    FX  " + str(fixed_bound) + "  0\n")
        outfile.write("2\n")
        outfile.write("    FX  0    " + str(fixed_bound) + "\n")
        outfile.write("    FX  " + str(fixed_bound) + "  0\n")
        outfile.write("2\n")
        outfile.write("    FX  0    " + str(fixed_bound) + "\n")
        outfile.write("    FX  " + str(fixed_bound) + "  0\n")
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


if __name__ == '__main__':
    
    if (len(sys.argv) != 2):
        print("\n> The size of the fixed boundary must be given on the command-line.")
        print("> Exiting...")
        sys.exit()
    
    # Parse the fixed_bound
    fixed_bound = sys.argv[1]
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
    
    md_setup_fixed_bounds(fixed_bound)
