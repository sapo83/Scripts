#!/usr/bin/env python

import random, string

### function with list of letters predefined
def randomseq(length):
   letters = ['A', 'C', 'G', 'T', '-']
   return ''.join(random.choice(letters) for i in range(length))

print(randomseq(10))

### function where the list of letters can be passed as an argument
def randomseqlibrary(length, library):
    letters = library
    return ''.join(random.choice(letters) for i in range(length))

base = ['A', 'C', 'G', 'T']
print(randomseqlibrary(10, base))
