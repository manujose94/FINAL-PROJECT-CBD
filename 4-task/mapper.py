#!/usr/bin/python2


import sys
import json
entry = {}
        
for line in sys.stdin:
    line = line.strip()
    # parse the incoming json 
    j = json.loads(line)

    if j != None:
    	try:
		if  len(str(j['review/profileName']))>1 and j['review/profileName'] != 'unknown':
			print "{0}\t{1}".format(j['review/profileName'],j['review/score'])
        except Exception as e: 
            	continue


