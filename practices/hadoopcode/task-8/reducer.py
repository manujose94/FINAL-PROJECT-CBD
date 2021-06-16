#!/usr/bin/python
import sys

getTotal = 0
oldKey = None
maxTotal=0;
maxItem=None;

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    #Get typeReq if we want filter by type request like GET	
    thisKey, thisTypeReq  = data_mapped

    if oldKey and oldKey != thisKey:
	if getTotal > maxTotal:
        	maxTotal=getTotal;
		maxItem=oldKey;
        oldKey = thisKey;
        getTotal = 0

    oldKey = thisKey
    getTotal += 1

if maxItem != None:
    print maxItem, "\t", maxTotal

