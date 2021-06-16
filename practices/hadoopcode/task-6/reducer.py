#!/usr/bin/python

import sys

getTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisReq  = data_mapped
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", getTotal
        oldKey = thisKey;
        getTotal = 0

    oldKey = thisKey
    getTotal += 1

if oldKey != None:
    print oldKey, "\t", getTotal

