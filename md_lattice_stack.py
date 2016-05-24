#!/usr/bin/env python

# This function reads the lattice.dat file and creates a larger supercell
# by stacking multiple copies.

# The user select the number of cells to stack in each direction, either on
# the command-line, or interactively.

# Kenny Jolley   May 2016  python 2

import sys

def md_lattice_stack(cells_x,cells_y,cells_z):
    # Input file
    file = open('lattice.dat', 'r')
    # Output file
    output_filename = "lattice_supercell_" + str(cells_x) + "_" + str(cells_y) + "_"+ str(cells_z) + ".dat"
    print output_filename
    outputfile = open(output_filename, 'w')

    # atoms
    l1st = file.readline()
    line1 = l1st.split()
    atoms = int(line1[0])
    # box
    l2nd = file.readline()
    line2 = l2nd.split()
    boxx = float(line2[0])
    boxy = float(line2[1])
    boxz = float(line2[2])
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
    # read atoms from input
    xval = [0 for x in xrange(atoms+1)]
    yval = [0 for x in xrange(atoms+1)]
    zval = [0 for x in xrange(atoms+1)]
    atomtype = [0 for x in xrange(atoms+1)]
    atomcharge = [0 for x in xrange(atoms+1)]
    counter = 1
    while 1:
        dataline = file.readline()
        if not dataline: break
    
        data = dataline.split()
        atomtype[counter] = data[0]
        xval[counter] = float(data[1])
        yval[counter] = float(data[2])
        zval[counter] = float(data[3])
        atomcharge[counter] = float(data[4])
        counter = counter + 1
    # print all cells
    for i in range(1,cellx+1):
        for j in range(1,celly+1):
            for k in range(1,cellz+1):
                for allatoms in range(1,atoms+1):
                    outputfile.write(str(atomtype[allatoms]) + ' \t' +
                                     str(xval[allatoms]+boxx*(i-1)) + ' \t' +
                                     str(yval[allatoms]+boxy*(j-1)) + ' \t' +
                                     str(zval[allatoms]+boxz*(k-1)) + ' \t' +
                                     str(atomcharge[allatoms]) + ' \n')
    file.close()
    outputfile.close()


if __name__ == '__main__':
    print("\nThis script reads the lattice.dat file and creates a larger supercell")
    print("by stacking multiple copies.\n")
    if len(sys.argv) == 4:
        cellx = int(sys.argv[1])
        celly = int(sys.argv[2])
        cellz = int(sys.argv[3])
        print("Cells = " + str(cellx) + " x " + str(celly) + " x " + str(cellz))
    else:
        print("You must set cell no. in x, y and z")
        cellx = raw_input('Enter no. of cells in x-dir: ')
        cellx = int(cellx)
        celly = raw_input('Enter no. of cells in y-dir: ')
        celly = int(celly)
        cellz = raw_input('Enter no. of cells in z-dir: ')
        cellz = int(cellz)
        print("Cells = " + str(cellx) + " x " + str(celly) + " x " + str(cellz))
    md_lattice_stack(cellx,celly,cellz)
