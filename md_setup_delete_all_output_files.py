#!/usr/bin/env python

# This script deletes all output files from the MD simulation
# User confirmation required.

# Kenny Jolley.   May 2016.   python 2/3

import os
import sys
# six is a module which patches over many of the python 2/3 common code base pain points.
from six.moves import input

def md_setup_delete_all_output_files():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("               WARNING")
    print("  This script deletes all MD output")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # dir setup
    initial_working_dir = os.getcwd()
    print("> Current directory: " + initial_working_dir +"\n")
    user_choice = input('Do you wish to do this? (yes/no)?: ')

    if (user_choice == 'yes'):
        print("> OK deleting all output files")

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
        # remove temp.txt if it exists
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
                return
            xyz_filename_zipped = xyz_file_prefactor + xyz_file_no + '.xyz.gz'
            xyz_filename_extracted = xyz_file_prefactor + xyz_file_no + '.xyz'
            # remove xyz_filename_zipped if it exists
            if (os.path.isfile(xyz_filename_zipped)):
                os.remove(xyz_filename_zipped)
            # remove xyz_filename_extracted if it exists
            if (os.path.isfile(xyz_filename_extracted)):
                os.remove(xyz_filename_extracted)
    else:
        print("> Function cancelled")
        print("> No files have been modified")

if __name__ == '__main__':
    md_setup_delete_all_output_files()
