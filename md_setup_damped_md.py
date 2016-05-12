#!/usr/bin/env python

# This function sets up the input file so that the
# md code will run a damped MD simulation.

# This script requires the simulation time to be passed as a parameter.

# set BEGIN in lbomd.IN  (This option starts a new simulation.)
# set EQUIL in lbomd.IN  (This option tells the md code to equilibrate.)

import os, sys

def md_setup_damped_md(simtime):
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
    outfile.write("DAMPMD    /* SELECT MINIMIZER (DAMPMD OR CONJGD) \n")
    simtime_str = str(float(simtime)) + '               '
    simtime_comment_str = '/* RELAXATION  TIME FOR DAMPED MD\n'
    simtime_line_str = simtime_str[:10] + simtime_comment_str
    outfile.write(simtime_line_str)
    outfile.write("0000.0    /* END TIME FOR THERMALISATION OF FULL SYSTEM (EXCET fixed atoms). \n")
    outfile.write("0000.0    /* END TIME FOR THERMALISATION OF CONSTRAINED SYSTEM (contraints \n")
    outfile.write("          /* are introduced in lattice.IN). \n")
    outfile.close()


if __name__ == '__main__':
    if( len(sys.argv) != 2):
        print("You must pass the simtime for damped MD to the script")
        sys.exit()
    md_setup_damped_md(sys.argv[1])

    