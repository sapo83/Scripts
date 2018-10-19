#!/usr/bin/env python

import gzip
import sys
from Bio import SeqIO

### 3 command line arguments - list of IDs to keep, gzipped fasta file to parse, output fasta file name
IDfile = sys.argv[1]
inputGZfasta = sys.argv[2]
outputFasta = sys.argv[3]

IDset = set()

### push all IDs into a set
with open(IDfile, 'r') as f2:
    for line2 in f2:
        line2 = line2.rstrip("\n")
        IDset.add(line2)

### open output file
out = open(outputFasta, 'w')

### open gzipped fasta file, loop through IDs in fasta, if found in ID list, print sequence to output file
with gzip.open(inputGZfasta, "rt") as f1:
    for record in SeqIO.parse(f1, "fasta"):
        for val in IDset:
            if val == record.id:
                SeqIO.write(record, out, "fasta")

### close output file
out.close()
