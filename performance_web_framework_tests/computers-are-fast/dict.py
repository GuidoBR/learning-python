#!/usr/bin/env python

# Number to guess: How many entries can
# we add to a dictionary in a second?

# Note: we take `i % 1000` to control
# the size of the dictionary

def f(NUMBER):
    d = {}
    for i in xrange(NUMBER):
        d[i % 1000] = i

import sys
f(int(sys.argv[1]))
