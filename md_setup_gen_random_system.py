#!/usr/bin/env python

# This function builds a random lattice based upon user input

# Lengths and positions are in units of [Angstroms]
# Density is in units of [g/cm3]


# TODO:
#  command-line input

# Kenny Jolley   Oct 2016  python 3

import sys, os
import math
import random
import md_constants
# six is a module which patches over many of the python 2/3 common code base pain points.
from six.moves import input

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

def md_setup_gen_random_system(sys_density,atom_id_list,atom_charge_list,atom_num_list):
    print("\n> Generating random system ...\n")
    print("> System density set to: " + str(sys_density) + " g/cm3")
    print("> Adding " + str(len(atom_id_list)) + " atom types")
    
    for i in range(len(atom_id_list)):
        print("> Adding " + str(atom_num_list[i]) + " " + 
              str(md_constants.atomic_name[atom_id_list[i]]) + " atoms, with charge " +
              str(atom_charge_list[i]))
              
    # total atoms         
    tot_atoms = 0
    for i in range(len(atom_id_list)):
        tot_atoms = tot_atoms + atom_num_list[i]
    print("> Total number of atoms in system: " + str(tot_atoms))
    if( (tot_atoms < 1) ):
        print(">  Error, no atoms added.")
        print(">  Exiting ....")
        sys.exit()
        
    # net charge
    net_charge = 0
    for i in range(len(atom_id_list)):
        net_charge = net_charge + atom_charge_list[i]*atom_num_list[i]
    print("> Net charge: " + str(net_charge))
    if( (net_charge > 0.001) or (net_charge < -0.001) ):
        print(">  Warning, system has non-zero net charge")
    
    # Total mass
    tot_mass = 0.0
    for i in range(len(atom_id_list)):
        tot_mass = tot_mass + atom_num_list[i]*md_constants.atomic_mass[atom_id_list[i]]
    print("> Total mass: " + str(tot_mass) + " amu")
    tot_mass = tot_mass*md_constants.amu
    print("> Total mass: " + str(tot_mass) + " kg")
    
    # calc boxsize
    sys_vol = tot_mass / (sys_density*1000.0)
    print("> System volume: " + str(sys_vol) + " m^3")
    sys_vol = sys_vol * 1e30
    print("> System volume: " + str(sys_vol) + " Ang^3")

    boxsize = math.pow(sys_vol, (1.0/3.0) )
    print("> System cubic side length: " + str(boxsize) + " Ang")
    print("> System cubic side length: " + str(boxsize/10.0) + " nm")
    
    
    # open file and write header
    file = open('lattice.dat', 'w+')
    print("\n> Opened file: " + file.name)
    file.write(str(tot_atoms) + "\n")
    file.write(str(boxsize) + "  " + str(boxsize)+ "  " + str(boxsize)+ " \n" )

    
    # generate list of random positions with no atom closer than 1 ang
    min_sep = 1
    # declare lists with first random position
    atomposx = [random.uniform(0, boxsize)]
    atomposy = [random.uniform(0, boxsize)]
    atomposz = [random.uniform(0, boxsize)]
    # create full list of random positions
    for i in range(1,tot_atoms):
    
        while 1:
            hit = 0
            # generate next random position
            new_x = random.uniform(0, boxsize)
            new_y = random.uniform(0, boxsize)
            new_z = random.uniform(0, boxsize)
            # check it is not within 1 ang of existing positions.
            for j in range(i):
                if( abs(new_x-atomposx[j])< min_sep):
                    if( abs(new_y-atomposy[j])< min_sep):
                        if( abs(new_z-atomposz[j])< min_sep):
                            print(str(i) + " hit xyz")
                            hit = 1
            if(hit== 0):
                break
        
        
        # append new random position to list
        atomposx.append(new_x)
        atomposy.append(new_y)
        atomposz.append(new_z)
    
    
    # write atoms to file
    write_counter = 0
    for i in range(len(atom_id_list)):
        for j in range(atom_num_list[i]):
            file.write(str(md_constants.atomic_symbol[atom_id_list[i]]) + "  " +
                       str(atomposx[write_counter]) + "  " +
                       str(atomposy[write_counter]) + "  " +
                       str(atomposz[write_counter]) + "  " +
                       str(atom_charge_list[i]) + "  " +
                       "\n")
            write_counter = write_counter + 1
    
    

if __name__ == '__main__':
    print("\n +--------------------------------------+")
    print(" | This script builds a random lattice  |")
    print(" +--------------------------------------+\n")
    
    # if command-line options are given, parse the data 
    if len(sys.argv) >1:
        # extract density
        sys_density = float(sys.argv[1])
        
        # determine number of atoms required
        num_sp = int( (len(sys.argv)-2)/2 )
        print(num_sp)
        
        # loop over all input atoms and check data
        
        # atom id
        atom_id = sys.argv[2]
        
        
        
    else:
        print(" You must provide some basic information about the system you wish to generate.\n")
        # Get density from the user
        while 1:
            sys_density = input('Enter required system density (g/cm3): ')
            if(is_number(sys_density)):
                sys_density = float(sys_density)
                if(sys_density <= 0):
                    print("The density must be greater than zero")
                else:
                    break
            else:
                print("You must enter a number")
                
        # Declare lists with first element
        atom_id_list = []   
        atom_charge_list = []
        atom_num_list = []
        
        # Get the atom data from user
        while 1:
            # Get atom id
            while 1:
                atom_id = input('Enter atom name, symbol or proton number: ')
                # if given an int, ensure it is a valid id no.
                if(is_int(atom_id)):
                    atom_id = int(atom_id)
                    if( (atom_id < 1) or (atom_id > 113) ):
                        print(" Atom id must be between 1 and 113")
                    else:
                        break
                else:
                    # if given two char atom symbol or element name, find the id no.
                    atom_id = md_constants.find_atomic_num(atom_id)
                    if( (atom_id < 1) or (atom_id > 113) ):
                        print("> Atom id must be between 1 and 113")
                    else:
                        break
            # get the charge
            while 1:
                atom_charge = input("Enter atomic charge for the " + str(md_constants.atomic_name[atom_id]) + " atoms: " )
                if(is_number(atom_charge)):
                    atom_charge = float(atom_charge)
                    break
                else:
                    print("You must enter a number")
            # get the number of atoms
            while 1:
                atom_num = input("Enter the required number of " + str(md_constants.atomic_name[atom_id]) + " atoms: " )
                if(is_int(atom_num)):
                    atom_num = int(atom_num)
                    if( (atom_num < 0) ):
                        print(" Number of atoms cannot be negative.")
                    else:
                        break
                else:
                    print("You must enter an integer")
            
            # Append data
            atom_id_list.append(atom_id)    
            atom_charge_list.append(atom_charge)
            atom_num_list.append(atom_num)
            
            # Do you wish to add another element?
            while 1:
                user_cont = input("Do you wish to add another element? (y/n): ")
                if( (user_cont.lower() == "y") or (user_cont.lower() == "n") ):
                    break
                else:
                    print("You must enter 'y' or 'n'")
        
            # Break loop if user no longer wants to add anymore atoms
            if(user_cont.lower() == "n"):
                break

    # function inputs:  density, array atom ids, array atom charges, array of no. of each atom. 
    md_setup_gen_random_system(sys_density,atom_id_list,atom_charge_list,atom_num_list)

# End
