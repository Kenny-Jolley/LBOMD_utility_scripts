#!/usr/bin/env python

# This function modifies both lbomd.IN and equilibrate.IN input files
# so that the MD code will run a conjugate gradient optimisation.

# set BEGIN in lbomd.IN  (This option starts a new simulation.)
# set EQUIL in lbomd.IN  (This option tells the md code to equilibrate.)
# set .T. in equilibrate.IN  (This option tells the md code to do relaxation.)
# set CONJGD in equilibrate.IN  (This option tells the md code to run a conjugate gradient optimisation.)
# reset everything else in equilibrate.IN to the default values.

# Kenny Jolley.   May 2016   python 2.7

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
