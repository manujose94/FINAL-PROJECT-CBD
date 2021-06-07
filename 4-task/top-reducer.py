#!/usr/bin/python

import sys
TotalScore = 0
maxTotalScore = 0
topUserReviews= None
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, thisScore = data_mapped
    if oldKey and oldKey != thisKey:
        if TotalScore > maxTotalScore:
            maxTotalScore=TotalScore
            topUserReviews=oldKey
        oldKey = thisKey;
        TotalScore = 0
        
    oldKey = thisKey
    TotalScore += 1
    

if oldKey != None and TotalScore > maxTotalScore:
	maxTotalScore=TotalScore
	topUserReviews=oldKey

if topUserReviews != None:
    print topUserReviews, "\t",maxTotalScore, "\t"

