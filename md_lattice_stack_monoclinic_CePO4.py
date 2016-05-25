#!/usr/bin/env python

# This function reads the lattice.dat file and creates a larger supercell
# by stacking multiple copies.

# The user selects the number of cells to stack in each direction, either on
# the command-line, or interactively.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#            This is for a monoclinic system
#       Angle beta set to value for optimised CePO4
#                    beta = 104.18
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# K. Jolley May 2016

import sys
import math

def md_lattice_stack_monoclinic_CePO4(cellx,celly,cellz):
    # hard-coding the angle beta
    beta_angle = 104.18
    angle_180_minus_b = 180 - beta_angle

    # read file data from lattice.dat
    file = open('lattice.dat', 'r')
    # Output file
    output_filename = "lattice_supercell_" + str(cells_x) + "_" + str(cells_y) + "_"+ str(cells_z) + ".dat"
    print(output_filename)
    outputfile = open(output_filename, 'w')
    
    # atoms
    line = file.readline()
    line = line.split()
    atoms = int(line[0])
    # box
    line = file.readline()
    line = line.split()
    boxx = float(line[0])
    boxy = float(line[1])
    boxz = float(line[2])
    newboxx = boxx * cellx
    newboxy = boxy * celly
    newboxz = boxz * cellz
    boxno = cellx * celly * cellz
    # atoms + boxsize
    print("oldatoms: " + str(atoms))
    print("newatoms: " + str(atoms*boxno))
    print("oldbox: " + str(boxx) + " " + str(boxy) + " " + str(boxz) )
    print("newbox: " + str(newboxx) + " " + str(newboxy) + " " + str(newboxz) )
    outputfile.write(str(atoms*boxno) + '\t' + '\n')
    outputfile.write(str(newboxx) + ' \t' + str(newboxy) + ' \t' + str(newboxz) + '\n')
    # set arrays
    xval = [0 for x in range(atoms+1)]
    yval = [0 for x in range(atoms+1)]
    zval = [0 for x in range(atoms+1)]
    atomtype = [0 for x in range(atoms+1)]
    atomcharge = [0 for x in range(atoms+1)]
    # read atoms from input
    for i in range(1,atoms+1):
        line = file.readline()
        if not line: break
    
        data = line.split()
        atomtype[i] = data[0]
        xval[i] = float(data[1])
        yval[i] = float(data[2])
        zval[i] = float(data[3])
        atomcharge[i] = float(data[4])
    file.close()

    # print all cells
    for i in range(1,cellx+1):
        for j in range(1,celly+1):
            for k in range(1,cellz+1):
                x_offset = (k-1) * boxz * math.cos(math.radians(angle_180_minus_b))
                for allatoms in range(1,atoms+1):
                    outputfile.write(str(atomtype[allatoms]) + ' \t' +
                                     str(xval[allatoms]+boxx*(i-1) - x_offset) + ' \t' +
                                     str(yval[allatoms]+boxy*(j-1)) + ' \t' +
                                     str(zval[allatoms]+boxz*(k-1)) + ' \t' +
                                     str(atomcharge[allatoms]) + ' \n')
    outputfile.close()

if __name__ == '__main__':
    print("\nThis script reads the lattice.dat file and creates a larger supercell")
    print("by stacking multiple copies.\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("            This is for a monoclinic system")
    print("       Angle beta set to value for optimised CePO4")
    print("                    beta = 104.18")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if len(sys.argv) == 4:
        cells_x = int(sys.argv[1])
        cells_y = int(sys.argv[2])
        cells_z = int(sys.argv[3])
        print("Cells = " + str(cells_x) + " x " + str(cells_y) + " x " + str(cells_z))
    else:
        print("You must set cell no. in x, y and z")
        cells_x = raw_input('Enter no. of cells in x-dir: ')
        cells_x = int(cells_x)
        cells_y = raw_input('Enter no. of cells in y-dir: ')
        cells_y = int(cells_y)
        cells_z = raw_input('Enter no. of cells in z-dir: ')
        cells_z = int(cells_z)
        print("Cells = " + str(cells_x) + " x " + str(cells_y) + " x " + str(cells_z))
    md_lattice_stack_monoclinic_CePO4(cells_x,cells_y,cells_z)
