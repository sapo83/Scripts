#!/usr/bin/env python

import random, string

def randomseq(length):
   letters = ['A', 'C', 'G', 'T', '-']
   return ''.join(random.choice(letters) for i in range(length))

print(randomseq(10))
