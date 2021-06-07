#!/usr/bin/python

import sys
totalReview = 0
maxtotalReview = 0
topGameReview= None
topIdProduct= None
oldKey = None
oldGame = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisGame = data_mapped
    if oldKey and oldKey != thisKey:
        if totalReview > maxtotalReview:
            maxtotalReview=totalReview
            topIdProduct=oldKey
            topGameReview=oldGame
        oldKey = thisKey;
        totalReview = 0
        
    oldGame =  thisGame
    oldKey = thisKey
    totalReview += 1
    
if oldKey != None and totalReview > maxtotalReview:
	maxtotalReview=totalReview
	topGameReview=oldGame
	topIdProduct=oldKey

if topGameReview != None:
    print topIdProduct, "\t",topGameReview, "\t",maxtotalReview

