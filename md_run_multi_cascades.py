#!/usr/bin/env python

# This is the general script that runs multiple cascades using input files
# and an input lattice given in a sub-directory named: md_input

# each run is contained within its own directory

# import python modules
import sys
import os
import shutil
import numpy as np
# import utility functions
import md_constants
from md_setup_production import md_setup_production
from md_setup_continue_production import md_setup_continue_production
from md_setup_simtime import md_setup_simtime
from md_setup_output_freq import md_setup_output_freq



# pick random 3d direction (equal area projection)
def pick_rand_dir():
    theta = 2 * np.pi * np.random.rand()
    z     = 2 * np.random.rand() - 1
    x = (np.sqrt(1-z*z))*np.cos(theta)
    y = (np.sqrt(1-z*z))*np.sin(theta)
    return x,y,z

# pick random point on 3d sphere centered on lattice centre, with radii= 0.45*box_
def pick_rand_point(box_x,box_y,box_z):
    theta = 2 * np.pi * np.random.rand()
    z     = 2 * np.random.rand() - 1
    x = (np.sqrt(1-z*z))*np.cos(theta)
    y = (np.sqrt(1-z*z))*np.sin(theta)
    
    x = x*box_x*0.45 + box_x*0.5
    y = y*box_y*0.45 + box_y*0.5
    z = z*box_z*0.45 + box_z*0.5
    return x,y,z


# create collisions.IN file
def md_setup_collision(specie_to_hit, col_energy,xpos,ypos,zpos,xdir,ydir,zdir,xbox,ybox,zbox):
    outfile = open("collisions.IN", 'w')
    line = str(xdir) + " " + str(ydir) + " " +  str(zdir) + "        /* INDX (TYPICALLY: 235 or 153)\n"
    outfile.write(line)
    line = str(col_energy)  + "          /* PROJECTIL_KE (in eV)\n"
    outfile.write(line)
    line = "T            /* SEARCH_FOR_PKA (PKA = PRIMARY KNOCK-ON ATOM)\n"
    outfile.write(line)
    #position of atom to hit
    line = str(xpos/xbox) + " " + str(ypos/ybox) + " " + str(zpos/zbox) + "     /* approximate PKA_SITE in lattice units (x*LX,y*LY,z*LZ)\n"
    outfile.write(line)
    #specie
    line = str(specie_to_hit)  + "           /* PKA atom symbol\n"
    outfile.write(line)
    line = "0            /* Timestep method: 0=variable (KE, default), 1=variable (speed), 2=fixed\n"
    outfile.write(line)
    outfile.close()

# read lattice header at input filename
def read_lattice_header(input_lattice_path):
    file = open(input_lattice_path, 'r')
    latline = file.readline()
    line = latline.split()
    atoms = int(line[0])
    latline = file.readline()
    line = latline.split()
    box_x = float(line[0])
    box_y = float(line[1])
    box_z = float(line[2])
    file.close()
    return atoms,box_x,box_y,box_z

# read lattice data into arrays
def read_lattice_data(input_lattice_path):
    pos_x = [0]
    pos_y = [0]
    pos_z = [0]
    specie_str = [0]
    atom_charge = [0]
    file = open(input_lattice_path, 'r')
    latline = file.readline()
    line = latline.split()
    atoms = int(line[0])
    latline = file.readline()
    atomno = 0
    # read file
    while 1:
        latline = file.readline()
        if not latline: break
        line = latline.split()
        atomno = atomno + 1
        specie_str.append(str(line[0]))
        pos_x.append(float(line[1]))
        pos_y.append(float(line[2]))
        pos_z.append(float(line[3]))
        atom_charge.append(float(line[4]))
    file.close()
    #error check
    if not (atoms==atomno):
        print "error, did not read expected no. of lines in lattice"
        print "atoms:  ", atoms
        print "atomno: ", atomno
    return specie_str,pos_x,pos_y,pos_z,atom_charge


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~            Begining of script                 ~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def md_run_multi_cascades(specie_to_hit,cascade_energy,cascade_time):
    # print the passed data
    print("running cascades")
    print("specie_to_hit:  " + str(specie_to_hit) )
    print("cascade_energy: " + str(cascade_energy) + " eV")
    print("cascade_time:   " + str(cascade_time) + " fs")
    # set variable types
    specie_to_hit = str(specie_to_hit)
    cascade_energy = float(cascade_energy)
    cascade_time = float(cascade_time)


    # dir setup
    initial_working_dir = os.getcwd()
    input_dir_name = initial_working_dir + '/md_input'
    output_dir_name_prefac = initial_working_dir + '/cascade_'
    input_lattice_path = input_dir_name + '/lattice.dat'
    input_LBOMD_path = input_dir_name + '/LBOMD.exe'


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
        outputfile.write('count\tstatus\n')
        outputfile.flush()
        os.fsync(outputfile.fileno())

    print("cascade_count:  " + str(counter) )


    # check for md_input dir, and that it contains relevant files
    if not (os.path.isdir(input_dir_name)):
        print("Directory: " + str(input_dir_name) + "  not found, exiting ...")
        sys.exit()
    if not (os.path.isfile(input_lattice_path)):
        print("Lattice.dat: " + str(input_lattice_path) + "  not found, exiting ...")
        sys.exit()
    if not (os.path.isfile(input_LBOMD_path)):
        print("LBOMD.exe: " + str(input_LBOMD_path) + "  not found, exiting ...")
        sys.exit()


    # read lattice header (in md_input dir)
    atoms,box_x,box_y,box_z = read_lattice_header(input_lattice_path)
    print("atoms:   " + str(atoms) )
    print("Lattice: " + str(box_x) + "  " + str(box_y) + "  " + str(box_z) + " Angstroms")
    sys.stdout.flush()


    # read atom data from lattice.dat
    specie_str,pos_x,pos_y,pos_z,atom_charge = read_lattice_data(input_lattice_path)

    # check that atom to hit exists
    atom_exists = 0
    for i in range(1,atoms+1):
        if( specie_to_hit == specie_str[i] ):
            atom_exists = 1
            break
    if( atom_exists == 0):
        print "Sanity check failed!"
        print "Did not find any atoms to hit"
        sys.exit()


    # loop runs inifinite cascades until the MD code is stopped
    while 1:
        # set counter and resume flag
        counter = counter + 1
        resume = 0
    
        # create directory for run no.=counter
        print "> Starting cascade no. ", counter
        output_dir_name  = output_dir_name_prefac + str(counter)
        # check if existing dir, otherwise create new one for this run
        if (os.path.isdir(output_dir_name)):
            print("> Existing directory found")
            output_FAILSAFE = output_dir_name + '/FAILSAFE.DAT.gz'
            if (os.path.isfile(output_FAILSAFE)):
                print("> Attempting to resume existing simulation")
                resume = 1
        else:
            print output_dir_name, "does not exist, creating new"
            # try except code ensures no race condition occurs
            # if dir is created elsewhere
            # should not be an issue, but is the safest way
            try:
                os.makedirs(output_dir_name)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise
            # we now copy files from input dir
            src_files = os.listdir(input_dir_name)
            for file_name in src_files:
                full_file_name = os.path.join(input_dir_name, file_name)
                if (os.path.isfile(full_file_name)):
                    shutil.copy2(full_file_name, output_dir_name)

        # change into dir
        os.chdir(output_dir_name)
        print "> We are now in: ", os.getcwd()

        # If resume flag, set md files to resume the simulation
        if(resume):
            # resume cascade
            md_setup_continue_production()
        else:
            # new simulation
            # choose random cascade starting location
            x,y,z = pick_rand_point(box_x,box_y,box_z)
        
            # compute cascade direction (points to center)
            xdir = 0.5*box_x - x
            ydir = 0.5*box_y - y
            zdir = 0.5*box_z - z
        
            # write collsions.IN file
            md_setup_collision(specie_to_hit,cascade_energy,x,y,z,xdir,ydir,zdir,box_x,box_y,box_z)
        
            # setup simtime
            md_setup_simtime(cascade_time)
            md_setup_production()
    
        # flush print statements
        sys.stdout.flush()
        # run the MD code
        os.system("./LBOMD.exe >/dev/null")
        #os.system("mpirun -np 16 LBOMD_MPI.exe >/dev/null")


        # determine if simulation completed successfully
        if (os.path.isfile("final-lattice.dat")):
            print("simulation of cascade " + str(counter) + " completed")
        else:
            # simulation did not finish correctly
            print("Cascade no. " + str(counter) + " did not finish")
            print("Exiting ... ")
            sys.stdout.flush()
            sys.exit()

        outputfile.write( str(counter) + '\tDone cascade \n')
        outputfile.flush()
        os.fsync(outputfile.fileno())




if __name__ == '__main__':
    # echo num of args
    print("Number of arguments given: " + str(len(sys.argv)-1))
    # Check that 3 are given
    if( len(sys.argv) != 4):
        print("Must use 3 arguments")
        print("specie_to_hit  (atom symbol)")
        print("cascade_energy (float, eV)")
        print("cascade_time (float, fs)")
        sys.exit()
    # parse command-line data
    
    # Parse the atom id
    atom_id = sys.argv[1]
    # if given an int, ensure it is a valid id no.
    try:
        atom_id = int(atom_id)
        if( (atom_id < 1) or (atom_id > 113) ):
            print("> Atom id must be between 1 and 113")
            print("> Exiting ...")
            sys.exit()
    except ValueError:
        # not an int, so try to lookup two char atom symbol or element name
        atom_id = md_constants.find_atomic_num(atom_id)
        if( (atom_id < 1) or (atom_id > 113) ):
            print("> Atom id must be between 1 and 113")
            print("> Exiting ...")
            sys.exit()
    # should now have a valid atom_id
    # so we can pass equiv atom symbol string to the function
    specie_to_hit = md_constants.atomic_symbol[atom_id]

    # ensure the cascade energy given is a positive number
    try:
        cascade_energy = float(sys.argv[2])
        if( (cascade_energy < 0) ):
            print("> The cascade energy must be a positive number.")
            print("> Exiting ...")
            sys.exit()
    except ValueError:
        print("> The cascade energy must be a positive number.")
        print("> Exiting ...")
        sys.exit()

    # ensure the cascade time given is a positive number
    try:
        cascade_time = float(sys.argv[3])
        if( (cascade_time < 0) ):
            print("> The cascade time must be a positive number.")
            print("> Exiting ...")
            sys.exit()
    except ValueError:
        print("> The cascade time must be a positive number.")
        print("> Exiting ...")
        sys.exit()


    # Call the md_run_multi_cascades function with the checked inputs
    md_run_multi_cascades(specie_to_hit,cascade_energy,cascade_time)


