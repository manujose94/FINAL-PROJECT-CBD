#!/usr/bin/python

import sys

getTotal = 0
findKey = '10.223.157.186'

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisGet  = data_mapped

    if thisKey == findKey:
        getTotal += 1

print findKey, "\t", getTotal

