#!/usr/bin/env python

# Takes a multi column mapping file & creates a two column file for easier use.

# command line arguments
# 1st arg = input file
# 2nd arg = output file
# 3rd arg = column number of ID for 1st column of outfile
# 4th arg = column number of ID for 2nd column of outfile

import sys

in_file = sys.argv[1]
out_file = sys.argv[2]
ID1_colnum = int(sys.argv[3])
ID2_colnum = int(sys.argv[4])

OUT = open(sys.argv[2], "w+")

with open(in_file) as map_file:
    next(map_file)
    for line in map_file:
        ID1 = line.split("\t")[ID1_colnum-1]
        ID2 = line.split("\t")[ID2_colnum-1]
        if(bool(ID1.strip())):
            OUT.write(str.join('', (str.join('\t', (ID1.strip(), ID2.strip())), "\n")))
        else:
            ID1 = "NA"
            OUT.write(str.join('', (str.join('\t', (ID1.strip(), ID2.strip())), "\n")))

OUT.close()
