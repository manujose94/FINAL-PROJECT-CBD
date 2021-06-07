#!/usr/bin/python

import sys
totalScore = 0
totalReview=0
oldKey = None
#Score has only 5 values (1.0,2.0,3.0,4.0,5.0)
sc = [0 for i in range(6)]
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisScore = data_mapped
    if oldKey and oldKey != thisKey:
        AVGScore=totalScore/totalReview
        print oldKey,"\t",AVGScore,"\t",totalReview,"\t",sc[1],":",sc[2],":",sc[3],":",sc[4],":",sc[5]
        oldKey = thisKey;
        sc = [0 for i in range(6)]
        totalScore = 0
        totalReview = 0

    oldKey = thisKey
    totalReview += 1
    sc[int(float(thisScore))] +=1
    totalScore += float(thisScore)
    
if oldKey != None:
	AVGScore=totalScore/totalReview
	sc[int(float(thisScore))] +=1
	print oldKey,"\t",AVGScore,"\t",totalReview,"\t",sc[1],":",sc[2],":",sc[3],":",sc[4],":",sc[5]
