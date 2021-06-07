#!/usr/bin/python

import sys
TotalScore = 0
TotalReview=0

oldKey = None
topAVGScoreGame=0
numTotalReview=0
nametopAVGScoreGame=''

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisScore = data_mapped
    if oldKey and oldKey != thisKey:
        mtopAVGScoreGame=TotalScore/TotalReview
        if mtopAVGScoreGame >= float(topAVGScoreGame) and TotalReview > numTotalReview :
            topAVGScoreGame=mtopAVGScoreGame
            nametopAVGScoreGame=oldKey
            numTotalReview=TotalReview;
        oldKey = thisKey;
        TotalScore = 0
        TotalReview = 0

    oldKey = thisKey
    TotalReview += 1
    TotalScore += float(thisScore)
    
if oldKey != None:
	mtopAVGScoreGame=TotalScore/TotalReview
	if mtopAVGScoreGame >= float(topAVGScoreGame) and TotalReview > numTotalReview :
		topAVGScoreGame=mtopAVGScoreGame
		nametopAVGScoreGame=oldKey
		numTotalReview=TotalReview;
print nametopAVGScoreGame,"\t", topAVGScoreGame,"\t", numTotalReview

