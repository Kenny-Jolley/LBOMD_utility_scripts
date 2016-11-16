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
    
    if (len(sys.argv) <> 2):
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




sys.exit()

# This function modifies both lbomd.IN and equilibrate.IN input files
# so that the MD code will run a conjugate gradient optimisation.

# set BEGIN in lbomd.IN  (This option starts a new simulation.)
# set EQUIL in lbomd.IN  (This option tells the md code to equilibrate.)
# set .T. in equilibrate.IN  (This option tells the md code to do relaxation.)
# set CONJGD in equilibrate.IN  (This option tells the md code to run a conjugate gradient optimisation.)
# reset everything else in equilibrate.IN to the default values.

# Kenny Jolley.   May 2016   python 2/3

import os

def md_setup_equilibrate():
    # open lbomd.IN files
    file = open('lbomd.IN', 'r')
    outfile = open('lbomdtemp.IN', 'w')
    #print "Opened file: ", file.name

    # read and edit lines
    line = file.readline()
    line = "BEGIN" + line[5:]
    outfile.write(line)
    line = file.readline()
    line = "EQUIL" + line[5:]
    outfile.write(line)
    # copy remainder of file
    while 1:
        line = file.readline()
        if not line: break
        outfile.write(line)
    file.close()
    outfile.close()
    # delete original file
    os.remove('lbomd.IN')
    # rename temp to original
    os.rename('lbomdtemp.IN', 'lbomd.IN')

    # write a new equilibration.IN file with required parameters
    # remove existing file if present.
    if (os.path.isfile("equilibration.IN")):
        os.remove('equilibration.IN')
    # Generate file
    outfile = open('equilibration.IN', 'w')
    outfile.write(".T.       /* RELAXATION .T. => YES ; .F. => NO\n")
    outfile.write("CONJGD    /* SELECT MINIMIZER (DAMPMD OR CONJGD) \n")
    outfile.write("0000.0    /* RELAXATION  TIME FOR DAMPED MD\n")
    outfile.write("0000.0    /* END TIME FOR THERMALISATION OF FULL SYSTEM (EXCET fixed atoms). \n")
    outfile.write("0000.0    /* END TIME FOR THERMALISATION OF CONSTRAINED SYSTEM (contraints \n")
    outfile.write("          /* are introduced in lattice.IN). \n")
    outfile.close()

if __name__ == '__main__':
    md_setup_equilibrate()
