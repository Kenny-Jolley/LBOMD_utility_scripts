#!/usr/bin/env python

# This function modifies both lbomd.IN and equilibration.IN input files,
# so that the MD code will thermalise the sytem at the user selected
# temperature for the user specified tme.

# set BEGIN in lbomd.IN  (This option starts a new simulation.)
# set EQUIL in lbomd.IN  (This option tells the md code to equilibrate.)
# set BERENDSEN in lbomd.IN  (This selects the berendsen thermostat.)

# We generate the equilibration.IN file
# set Relaxation to .F. in equilibration.IN
# set Thermalisation time in equilibration.IN

# User can select options on the command-line (or set values interactively).
# Useage:   md_setup_thermalise.py  sim_temp  sim_time

# user set temperature

# Kenny Jolley.   May 2016.   python 2

import os, sys

def md_setup_thermalise(sim_temp,sim_time):
    print("> Themostat set to: " + str(sim_temp) + " K")
    print("> Thermalisation time: " + str(sim_time) + " fs")
    
    # open lbomd.IN files
    file = open('lbomd.IN', 'r')
    outfile = open('lbomdtemp.IN', 'w')
    #print("Opened file: " + file.name)

    # read and edit lines
    line = file.readline()
    line = "BEGIN" + line[5:]
    outfile.write(line)
    line = file.readline()
    line = "EQUIL" + line[5:]
    outfile.write(line)
    for i in range (1,11):
        line = file.readline()
        outfile.write(line)
    line = file.readline()
    line = "BERENDSEN    " + line[13:]
    outfile.write(line)
    line = file.readline()
    sim_temp = float(sim_temp)
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

    # write a new equilibration.IN file with required parameters
    # remove existing file if present.
    if (os.path.isfile("equilibration.IN")):
        os.remove('equilibration.IN')
    # Generate file
    outfile = open('equilibration.IN', 'w')
    outfile.write(".F.       /* RELAXATION .T. => YES ; .F. => NO\n")
    outfile.write("CONJGD    /* SELECT MINIMIZER (DAMPMD OR CONJGD) \n")
    outfile.write("0000.0    /* RELAXATION  TIME FOR DAMPED MD\n")
    sim_time = float(sim_time)
    simtime_str = str(sim_time) + '             '
    line = "0000.0    /* END TIME FOR THERMALISATION OF FULL SYSTEM (EXCET fixed atoms). \n"
    line = simtime_str[:10] + line[10:]
    outfile.write(line)
    #outfile.write("0000.0    /* END TIME FOR THERMALISATION OF FULL SYSTEM (EXCET fixed atoms). \n")
    outfile.write("0000.0    /* END TIME FOR THERMALISATION OF CONSTRAINED SYSTEM (contraints \n")
    outfile.write("          /* are introduced in lattice.IN). \n")
    outfile.close()

    print("\n> Thermalisation options set, you can now run the MD code")



if __name__ == '__main__':
    if( len(sys.argv) == 3):
        print("> 2 values passed on the command-line")
        md_setup_thermalise(sys.argv[1],sys.argv[2])
    else:
        sim_temp = raw_input("Enter temperature: ")
        sim_temp = float(sim_temp)
        sim_time = raw_input("Enter thermalisation time (fs): ")
        sim_time = float(sim_time)
        md_setup_thermalise(sim_temp,sim_time)


