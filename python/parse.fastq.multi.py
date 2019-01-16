#!/usr/bin/env python

import multiprocessing
import sys
from itertools import izip_longest
from multiprocessing import Manager

### command line input
IDlist = sys.argv[1]  ### IDs to keep (with no @ symbol in front)
inFastq = sys.argv[2] ### fastq file to parse
outFastq = sys.argv[3]  ### output fastq filename

manager = Manager()
idList = list()
resList = list()

globalList = manager.list([])

### define functions
def multifunc(str): ### match fastq record ID to ID in list
    if str[0].rstrip("\n").split()[0] in idList:
        globalList.append(str)
    return

def grouper(iterable, n): ### get lines in file 4 at a time
    args = [iter(iterable)] * n
    return izip_longest(*args)

### read ID list into list object
with open(IDlist, 'r') as f1:
    for line1 in f1:
        line1 = line1.rstrip("\n")
        newID = "@" + line1
        idList.append(newID)

### set number of processes to run concurrently
pool = multiprocessing.Pool(processes=5)

with open(inFastq, 'r') as f1:
    for lines in grouper(f1, 4):
        pool.map(multifunc, lines)  ### run ID match function on each record

pool.close()     ### close pool
pool.join()     ### join all pool processes

### print results to output fastq
with open(outFastq, 'w') as f1: 
    for val in globalList:
        for val2 in val:
            f1.write(val2)
