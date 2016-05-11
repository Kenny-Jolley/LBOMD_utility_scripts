#!/usr/bin/env python

# This function sets options in lbomd.IN so that the md code
# continues an existing simulation.

# set CNTIN in lbomd.IN  (This option continues an existing simulation.)
# set PRODU in lbomd.IN  (This option tells the md code to do a normal production run.)
# set NO_THERMOSTAT in lbomd.IN  (This option ensures that no thermostat is applied.)

# Kenny Jolley.   May 2016   python 2.7

import os

def md_setup_continue_production():
    # open lbomd.IN files
    file = open('lbomd.IN', 'r')
    outfile = open('lbomdtemp.IN', 'w')
    #print "Opened file: ", file.name

    # read and edit lines
    line = file.readline()
    line = "CNTIN" + line[5:]
    outfile.write(line)
    line = file.readline()
    line = "PRODU" + line[5:]
    outfile.write(line)
    for i in range (1,11):
        line = file.readline()
        outfile.write(line)
    line = file.readline()
    line = "NO_THERMOSTAT" + line[13:]
    outfile.write(line)
    line = file.readline()
    sim_temp = float(0.0)
    simtemp_str = str(sim_temp) + '             '
    line = simtemp_str[:12] + line[12:]
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
    #print "Done"

if __name__ == '__main__':
    md_setup_continue_production()
