#!/usr/bin/python2
import sys
import json

entry = {}
for line in sys.stdin:
    line = line.strip()
    j = json.loads(line)
    if j != None:
    	try:
        	print "{0}\t{1}".format(j['product/title'], j['review/score'])
        except Exception as e: 
            	continue
 
