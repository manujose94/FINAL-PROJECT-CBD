#!/usr/bin/python

import sys

def reduce(findItem,separator='\t'):
    oldKey = None
    foundItem=None
    titleName=findItem
    findItem= findItem.lower().replace("'", "")
    for line in sys.stdin:
        data_mapped = line.strip().split(separator)
        if len(data_mapped) != 3:
            # Something has gone wrong. Skip this line.
            continue
        #title, score
        thisKey, thisScore, thisTime = data_mapped

        if oldKey and oldKey != thisKey:
            oldKey = thisKey;
            foundItem=None;


        oldKey = thisKey.lower().replace("'", "")
        if oldKey == findItem:
            print titleName, "\t", thisScore, "\t", thisTime


if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    if (arguments >= 1):
        reduce(sys.argv[1])
    else:
        reduce("Age of Empires 2: Age of Kings")



