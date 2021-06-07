#!/usr/bin/python
import sys

TotalScore = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisScore = data_mapped
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", TotalScore
        oldKey = thisKey;
        TotalScore = 0

    oldKey = thisKey
    TotalScore += 1

if oldKey != None:
    print oldKey, "\t", TotalScore

