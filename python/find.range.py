#!/usr/bin/env python

### input - list of numbers
### output - min & max, tab separated

import sys

file = sys.argv[1]

with open(file, 'r') as f:
    x = f.readlines()

max = max(x).rstrip("\n")
min = min(x).rstrip("\n")

print(min + "\t" + max)
