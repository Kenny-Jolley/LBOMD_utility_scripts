#!/usr/bin/env python

# This script enables many instances of md_run_multi_cgmins.py to be farmed out on a HPC.

# This script is specific for CARBON systems.

# Script requires a 'densitysim_input' directory containing LBOMD.exe.
# Carbon reaxFF input files are generated automattically.

# Usage:
#  md_run_multi_cgmins_carbon_HPC_farm.py  job_no  density_min  density_step  Num_carbon_atoms



import sys
import os
import shutil
from md_setup_gen_carbon_input_files import md_setup_gen_carbon_input_files


# set-up for this job
if( len(sys.argv) != 5):
    print("Must use 4 arguments")
    print(">  Usage:")
    print("   md_run_multi_cgmins_carbon_HPC_farm.py  job_no  density_min  density_step  Num_carbon_atoms")
    print("job number =  (integer  [0 -  (n-1)] )")
    sys.exit()
job_number = int(sys.argv[1])
density_min = int(sys.argv[2])
denstiy_step = int(sys.argv[3])
c_atoms = int(sys.argv[4])
sys_struct_string  = "C_ 0 " + str(c_atoms)


print("Helloworld from md_run_multi_cgmins_carbon_HPC_farm.py:  " + str(job_number))
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
# generate input files
md_setup_gen_carbon_input_files()

print("Running multi_cgmins simulations")
density = sim/1000.0
passed_vars_string = ( str(density) + " " + str(sys_struct_string) +  " > command_line_out.txt" )
md_run_string = 'md_run_multi_cgmins.py ' + passed_vars_string
print(md_run_string)
sys.stdout.flush()
os.system(md_run_string)  # should not return unless multimin script fails

sys.exit()

