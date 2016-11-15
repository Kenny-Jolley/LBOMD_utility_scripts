#!/usr/bin/env python

# This function sets the output frequency of the MD code for writing data files.


# Kenny Jolley.   Nov 2016   python 2/3

import os
import sys


def md_setup_output_freq(out_freq):
    # check a positive number is given
    try:
        out_freq = float(out_freq)
    except ValueError:
        print("\n> ERROR in md_setup_output_freq.py")
        print(">  out_freq must be a positive number , exiting ... ")
        sys.exit()
    if( (out_freq == 0) or (out_freq < 0) ):
        print("\n> ERROR in md_setup_output_freq.py")
        print(">  out_freq must be a positive number , exiting ... ")
        sys.exit()
    
    # check lbomd.IN exists and open it
    if (os.path.isfile("lbomd.IN")):
        file = open('lbomd.IN', 'r')
        outfile = open('lbomdtemp.IN', 'w')
    else:
        print("\n> ERROR in md_setup_output_freq.py")
        print(">  Could not find file: lbomd.IN ")
        print(">   exiting ... ")
        sys.exit()

    # string with output freq
    out_freq_str = str(out_freq) + "                  "

    # read and output lines straight away that do not need changing
    for i in range(16):
        line = file.readline()
        outfile.write(line)

    # modify the output freq line, and write to new file
    line = file.readline()
    line = out_freq_str[:12] + line[12:]
    outfile.write(line)

    # copy the remainder of the file, to the new file
    while 1:
        line = file.readline()
        if not line: break
        outfile.write(line)
    file.close()
    outfile.close()

    # overwrite the old file with the new one
    # delete original file
    os.remove('lbomd.IN')
    # rename temp to original
    os.rename('lbomdtemp.IN', 'lbomd.IN')


if __name__ == '__main__':
    if( len(sys.argv) != 2):
        print("\n> ERROR in md_setup_output_freq.py")
        print(">  You must pass the output frequency (in fs) to the script.")
        print(">   exiting ... ")
        sys.exit()
    md_setup_output_freq(sys.argv[1])

