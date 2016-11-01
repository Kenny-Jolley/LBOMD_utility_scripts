#!/usr/bin/env python

# This script quenches multiple lattices with properties read from the command-line.


# example inputs
#  quench a sequence of 2016 atom glass systems
#    md_run_multi_cgmins.py 2.1 si 1.89 392 b 1.4175 336 O_ -0.945 1288
#  quench a sequence of 2000 atom carbon systems
#    md_run_multi_cgmins.py 2.1 C_ 0.0 2000



# import python modules
from __future__ import print_function
import sys
import os
import shutil
import math
import random

# import utility functions
import md_constants
from md_setup_simtime import md_setup_simtime
from md_setup_equilibrate import md_setup_equilibrate
from md_setup_continue_production import md_setup_continue_production
from md_setup_gen_random_system import md_setup_gen_random_system
from md_setup_production import md_setup_production

def print_usage():
    print("\n> Usage ")
    print("> ~~~~~ ")
    print(">  Command-line input:")
    print(">   md_run_multi_cgmins.py density  atom_N_id  atom_N_charge  atom_N_num ")
    print(">  Example :")
    print(">   md_run_multi_cgmins.py 1.9 C_ 0 1000 ")
    print(">   md_run_multi_cgmins.py 1.9 C_ 0 1000 O_ 0 100 H_ 0 200")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Check some file requirements, exit if files not available
if not (os.path.isfile("buck.IN")):
    print("> Error, a required file is not present")
    print(">  buck.IN  not found ...")
    sys.exit()
if not (os.path.isfile("collisions.IN")):
    print("> Error, a required file is not present")
    print(">  collisions.IN  not found ...")
    sys.exit()
if not (os.path.isfile("conjugate_gradient.IN")):
    print("> Error, a required file is not present")
    print(">  conjugate_gradient.IN  not found ...")
    sys.exit()
if not (os.path.isfile("dpmta.IN")):
    print("> Error, a required file is not present")
    print(">  dpmta.IN  not found ...")
    sys.exit()
if not (os.path.isfile("equilibration.IN")):
    print("> Error, a required file is not present")
    print(">  equilibration.IN  not found ...")
    sys.exit()
if not (os.path.isfile("lattice.IN")):
    print("> Error, a required file is not present")
    print(">  lattice.IN  not found ...")
    sys.exit()
if not (os.path.isfile("lbomd.IN")):
    print("> Error, a required file is not present")
    print(">  lbomd.IN  not found ...")
    sys.exit()
if not (os.path.isfile("potfor.IN")):
    print("> Error, a required file is not present")
    print(">  potfor.IN  not found ...")
    sys.exit()
if not (os.path.isfile("LBOMD.exe")):
    print("> Error, a required file is not present")
    print(">  LBOMD.exe  not found ...")
    sys.exit()


# You must pass command-line arguments for the system
# if command-line options are given, parse the data
if len(sys.argv) >1:
    
    if(len(sys.argv) < 5):
        print("> Error, to few arguments given")
        print_usage()
        sys.exit()
    
    # Declare lists with first element
    atom_id_list = []
    atom_charge_list = []
    atom_num_list = []
        
    print("> Processing command-line input")
        
    # extract density
    sys_density = float(sys.argv[1])
        
    # determine number of atoms required
    num_sp = int( (len(sys.argv)-2)/3 )
    print("> Total number of atomic species: " + str(num_sp) )
        
        
    # loop over all input atoms and check data
    for i in range(num_sp):
        #print(str(i))
            
        # Parse the atom id
        atom_id = sys.argv[2+i*3]
        # if given an int, ensure it is a valid id no.
        if(is_int(atom_id)):
            atom_id = int(atom_id)
            if( (atom_id < 1) or (atom_id > 113) ):
                print("> Atom id must be between 1 and 113")
                print("> Exiting ...")
                print_usage()
                sys.exit()
        else:
            # if given two char atom symbol or element name, find the id no.
            atom_id = md_constants.find_atomic_num(atom_id)
            if( (atom_id < 1) or (atom_id > 113) ):
                print("> Atom id must be between 1 and 113")
                print("> Exiting ...")
                print_usage()
                sys.exit()
        # append the found atom id to list
        atom_id_list.append(atom_id)
            
        # Parse the atom charge
        atom_charge = sys.argv[3+i*3]
        if(is_number(atom_charge)):
            atom_charge = float(atom_charge)
        else:
            print("> Atom charge must be a number.")
            print("> Exiting ...")
            print_usage()
            sys.exit()
        # append the found atom charge to list
        atom_charge_list.append(atom_charge)
            
        # Parse the number of atoms
        atom_num = sys.argv[4+i*3]
        # atom num must be a positive integer
        if(is_int(atom_num)):
            atom_num = int(atom_num)
            if( (atom_num < 0) ):
                print(" Number of atoms cannot be negative.")
                print("> Exiting ...")
                print_usage()
                sys.exit()
        else:
            print("Number of atoms must be a positive integer ")
            print("> Exiting ...")
            print_usage()
            sys.exit()
        # append the number of atoms to list
        atom_num_list.append(atom_num)
        
    print(str(atom_id_list))
    print(str(atom_charge_list))
    print(str(atom_num_list))
# else exit, display usage
else:
    print(" You must provide some basic information about the system you wish to generate.\n")
    print_usage()
    sys.exit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~            Begining of script                 ~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# check for existing output, set counter so we dont over-write files
counter = 0
if (os.path.isfile("output.txt")):
    outputfile = open('output.txt', 'r')
    while 1:
        line = outputfile.readline()
        if not line: break
        counter = counter + 1
    outputfile.close()
    outputfile = open('output.txt', 'a')
    counter = counter - 1   #  do this to account for header of file
else:
    outputfile = open('output.txt', 'w')
    outputfile.write('count    energy\n')
    outputfile.flush()
    os.fsync(outputfile.fileno())


# loop do infinite quenches
while 1:
    counter = counter + 1
    if (os.path.isfile("final-lattice.dat")):
        # delete final-lattice.dat
        os.remove('final-lattice.dat')

    # check if broken run exists (resume if so)
    if( (os.path.isfile("cascades.OUT"))*(os.path.isfile("lattice.dat"))*(os.path.isfile("FAILSAFE.DAT.gz")) ):
        # set prodution and simtime
        md_setup_simtime(1200000)
        # set MD code to resume a simulation
        md_setup_continue_production()
        
        # run md code to quench system
        print("resuming quench no. " + str(counter) )
        # flush print statements
        sys.stdout.flush()
        os.system("./LBOMD.exe >/dev/null")
    else:
        # we are begining a new quench

        # generate random lattice
        md_setup_gen_random_system(sys_density,atom_id_list,atom_charge_list,atom_num_list)
        
        # set prodution and simtime
        md_setup_production()
        md_setup_simtime(1200000)
        
        # run md code to quench system
        print("running quench no. " + str(counter))
        # flush print statements
        sys.stdout.flush()
        os.system("./LBOMD.exe >/dev/null")
            
    # determine if simulation completed
    if (os.path.isfile("final-lattice.dat")):
        # quench simulation complete
        # delete initial random lattice.dat
        os.remove('lattice.dat')
        # rename final-lattice.dat to lattice.dat
        os.rename('final-lattice.dat', 'lattice.dat')
        # delete cascades.OUT
        os.remove('cascades.OUT')
        # delete FAILSAFE
        if (os.path.isfile("FAILSAFE.DAT.gz")):
            os.remove('FAILSAFE.DAT.gz')
        if (os.path.isfile("FAILSAFE.DAT")):
            os.remove('FAILSAFE.DAT')
    else:
        # simulation did not finish correctly
        print("quench no. " + str(counter) + " did not finish")
        print("Exiting ... ")
        sys.stdout.flush()
        sys.exit()
    
    # Quench should be complete, now minimise to 0 K using conjugate gradient method
    # set equilibration
    md_setup_equilibrate()
    # run md code to minimize system
    print("minimising quench no. "+  str(counter) )
    os.system("./LBOMD.exe >/dev/null")
    # only needed if testing with minimising
    #shutil.copy2('lattice.dat', 'final-lattice.dat')
    
    # now have minimised lattice
    # delete lattice.dat
    os.remove('lattice.dat')
    # save a copy of the final structure
    final_struct_filename = 'lattice_cgmin_' + str(counter) + '.dat'
    shutil.copy2('final-lattice.dat', final_struct_filename)

    # record the minimum energy
    # rename final-lattice.dat to lattice.dat
    os.rename('final-lattice.dat', 'lattice.dat')
    # set prodution and simtime
    md_setup_production()
    md_setup_simtime(1.0)
    # run 1fs to get energy
    os.system("./LBOMD.exe > temp.txt")
    
    # open file
    file = open('temp.txt', 'r')
    for i in range(3):
        line = file.readline()
    energy = line.split()

    outputfile.write( str(counter) + '      ' + str(energy[3]) +'\n' )
    outputfile.flush()
    os.fsync(outputfile.fileno())
    file.close()

    # Delete output files
    # remove cascades.OUT if it exists
    if (os.path.isfile("cascades.OUT")):
        os.remove('cascades.OUT')
    # remove thermalize.OUT if it exists
    if (os.path.isfile("thermalize.OUT")):
        os.remove('thermalize.OUT')
    # remove animation-input.xyz if it exists
    if (os.path.isfile("animation-input.xyz")):
        os.remove('animation-input.xyz')
    # remove animation-input.xyz.lock if it exists
    if (os.path.isfile("animation-input.xyz.lock")):
        os.remove('animation-input.xyz.lock')
    # remove animation-reference.xyz if it exists
    if (os.path.isfile("animation-reference.xyz")):
        os.remove('animation-reference.xyz')
    # remove FAILSAFE.DAT if it exists
    if (os.path.isfile("FAILSAFE.DAT.gz")):
        os.remove('FAILSAFE.DAT.gz')
    # remove FAILSAFE.DAT if it exists
    if (os.path.isfile("FAILSAFE.DAT")):
        os.remove('FAILSAFE.DAT')
    # remove final-lattice.dat if it exists
    if (os.path.isfile("final-lattice.dat")):
        os.remove('final-lattice.dat')
    # remove final-lattice.xyz if it exists
    if (os.path.isfile("final-lattice.xyz")):
        os.remove('final-lattice.xyz')
    # remove final-lattice.xyz if it exists
    if (os.path.isfile("final-lattice.xyz.gz")):
        os.remove('final-lattice.xyz.gz')
    # remove ReaxFF_report.OUT if it exists
    if (os.path.isfile("ReaxFF_report.OUT")):
        os.remove('ReaxFF_report.OUT')
    # remove animation-reference.xyz.gz if it exists
    if (os.path.isfile("animation-reference.xyz.gz")):
        os.remove('animation-reference.xyz.gz')
    # remove temp.txt if it exists
    if (os.path.isfile("temp.txt")):
        os.remove('temp.txt')
    # remove fort.665 if it exists
    if (os.path.isfile("fort.665")):
        os.remove('fort.665')
    # remove all the xyz files
    # determine their name
    lbomd_filename = 'lbomd.IN'
    file = open(lbomd_filename, 'r')
    latline = file.readline()
    latline = file.readline()
    latline = file.readline()
    latline = file.readline()
    line = latline.split()
    xyz_file_prefactor = str(line[0])
    file.close()
    print("> xyz_file_prefactor: " + xyz_file_prefactor)
    for i in range(10000):
        if (i < 10):
            xyz_file_no = '000' + str(i)
        elif (i < 100):
            xyz_file_no = '00' + str(i)
        elif (i < 1000):
            xyz_file_no = '0' + str(i)
        elif (i < 10000):
            xyz_file_no = str(i)
        else:
            print("exceeding 10000 files - exiting")
           
        xyz_filename_zipped = xyz_file_prefactor + xyz_file_no + '.xyz.gz'
        xyz_filename_extracted = xyz_file_prefactor + xyz_file_no + '.xyz'
        # remove xyz_filename_zipped if it exists
        if (os.path.isfile(xyz_filename_zipped)):
            os.remove(xyz_filename_zipped)
        # remove xyz_filename_extracted if it exists
        if (os.path.isfile(xyz_filename_extracted)):
            os.remove(xyz_filename_extracted)

    # flush print statements
    sys.stdout.flush()

sys.exit()

