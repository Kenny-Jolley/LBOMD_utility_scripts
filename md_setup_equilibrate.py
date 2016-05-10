#!/usr/bin/env python

# This function modifies both lbomd.IN and equilibrate.IN input files
# so that the MD code will run a conjugate gradient optimisation.

# set BEGIN in lbomd.IN  (This option starts a new simulation.)
# set EQUIL in lbomd.IN  (This option tells the md code to equilibrate.)
# set .T. in equilibrate.IN  (This option tells the md code to do relaxation.)
# set CONJGD in equilibrate.IN  (This option tells the md code to run a conjugate gradient optimisation.)

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

    # open equilibration files
    file = open('equilibration.IN', 'r')
    outfile = open('equilibrationtemp.IN', 'w')
    #print "Opened file: ", file.name
    line = file.readline()
    line = ".T." + line[3:]
    outfile.write(line)
    line = file.readline()
    line = "CONJGD" + line[6:]
    outfile.write(line)
    # copy remainder of file
    while 1:
        line = file.readline()
        if not line: break
        outfile.write(line)
    file.close()
    outfile.close()
    # delete original file
    os.remove('equilibration.IN')
    # rename temp to original
    os.rename('equilibrationtemp.IN', 'equilibration.IN')

    #print "set EQUIL in lbomd.IN"
    #print "set CONJGD to .T. in equilibrate.IN"
    #print "Done"

if __name__ == '__main__':
    md_setup_equilibrate()
