#!/usr/bin/python
import sys

totalScore = 0
highestScore= 0
lowestScore=0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thisUser, thisScore = data_mapped
    if oldKey and oldKey != thisUser:
    	print oldKey, "\t",totalScore, "\t",lowestScore, "\t",highestScore
	oldKey = thisUser;
	totalScore = 0
	lowestScore = 0
	highestScore = 0
        

    oldKey = thisUser
    totalScore += 1
    if float(lowestScore) > float(thisScore):
    	lowestScore = thisScore
    elif float(highestScore) < float(thisScore):
    	highestScore = thisScore
    

if oldKey != None:
    print oldKey, "\t",totalScore, "\t",lowestScore, "\t",highestScore

