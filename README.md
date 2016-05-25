# LBOMD_utility_scripts
A collection of utility scripts for use with the Loughborough MD code

These python scripts are only useful to me and others working with the LBOMD code.


## Installation

Clone the repository to a directory of your choice, and add this directory to your path.

To make the python scripts executable, run

`chmod +x md_*`


## Usage

The scripts can be called directly and passed options on the command line, or imported into other scripts.

### md setup

`md_setup_continue_production.py`  
This function sets options in lbomd.IN so that the md code continues an existing simulation.

`md_setup_damped_md.py`  
This function sets up the input files so that the md code will run a damped MD simulation.

`md_setup_delete_all_output_files.py`  
This function will delete all files output by the MD code.

`md_setup_equilibrate.py`  
Sets options in the input files so that the md code optimises the system using the conjugate gradient method.

`md_setup_gen_carbon_input_files.py`   
Generates a set of default input files for carbon systems.

`md_setup_production.py`  
This function sets options in lbomd.IN so that the md code begins a normal production run.

`md_setup_simtime.py  simtime`  
Sets the maximum simulation time to "simtime".

`md_setup_thermalise/py  sim_temp  sim_time`
This function sets options in lbomd.IN and equilibration.IN so that the md code thermalises a system.  User selects the temperature and thermalisation time.

### lattice utility

`md_lattice_stack.py  X Y Z`  
This function reads the lattice.dat file and creates a larger supercell by stacking multiple copies.  The number of cells in x, y, and z can be specified on the command-line, or entered interactively.  Orthorhombic lattices only.



### lattice generators



