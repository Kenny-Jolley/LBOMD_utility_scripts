#!/usr/bin/env python

# This function sets the simtime in lbomd.IN (note max 12 chars)


# set PRODU in lbomd.IN  
# set simtime in lbomd.IN (note max 12 chars)

# Kenny Jolley.   May 2016.   python 2.7.3

import os
import sys


def md_setup_simtime():   

    # open lbomd.IN files
    file = open('lbomd.IN', 'r')
    outfile = open('lbomdtemp.IN', 'w')
    #print "Opened file: ", file.name

    if( len(sys.argv) != 2):
        print("Must pass simtime to the script")
        exit()

    simtime = sys.argv[1]
    simtime_str = str(simtime) + '             '

    # read and edit lines
    line = file.readline()
    outfile.write(line)
    line = file.readline()
    line = "PRODU" + line[5:]
    outfile.write(line)
    for i in range(5):
        line = file.readline()
        outfile.write(line)
    line = file.readline()
    line = simtime_str[:12] + line[12:]
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
    #print "set PRODU in lbomd.IN"
    #print "set runtime in lbomd.IN to: ", simtime_str[:12]


if __name__ == '__main__':
    md_setup_simtime()
    