#!/usr/bin/env python

# This script enables many instances of md_run_multi_cgmins.py to be farmed out on a HPC.

# Script requires an 'md' directory containing LBOMD.exe and all other input files.

# script must be called with a number 0 - (n-1) to signify which job to do

# control info for structure and density range, is hard coded.


import sys
import os
import shutil

#--------------------------------
#- Inputs to farm prog
sys_struct_string  = 'C_ 0 200 '
# density range
density_min = 1700    # density for job 0
denstiy_step = 100    # ie density for job n  is: density_min + n*denstiy_step
#---------------------------------


# set-up for this job
if( len(sys.argv) != 2):
    print("Must use 1 argument")
    print("job number  (integer  0 -  (n-1) )")
    sys.exit()
job_number = int(sys.argv[1])
print("Helloworld from md_run_multi_cgmins_graphite_HPC_farm.py:  " + str(job_number))
sim = density_min + job_number*denstiy_step
print("Density: " + str(sim))

# dir setup
initial_working_dir = os.getcwd()
input_dir_name = initial_working_dir + '/densitysim_input'
output_dir_name_prefac = initial_working_dir + '/rho'

print(input_dir_name)
print(output_dir_name_prefac)

# check we have the input dir
if (os.path.isdir(input_dir_name)):
    print("Found densitysim_input dir")
else:
    print("densitysim_input dir does not exist, exiting")
    sys.exit()


# setup the directory for this run
output_dir_name  = output_dir_name_prefac + str(sim)
print(output_dir_name)
if (os.path.isdir(output_dir_name)):
    print("Found existing output_dir_name")
else:
    print("output_dir does not exist, creating new")
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
# submit md_run_multi_cgmins with above data and density
output_dir_name  = output_dir_name_prefac + str(sim)
os.chdir(output_dir_name)
print(os.getcwd())
print("Running multi_cgmins simulations")
density = sim/1000.0
passed_vars_string = ( str(density) + " " + str(sys_struct_string) +  " > command_line_out.txt" )
md_run_string = 'md_run_multi_cgmins.py ' + passed_vars_string
print(md_run_string)
sys.stdout.flush()
os.system(md_run_string)  # should not return unless multimin script fails

sys.exit()

