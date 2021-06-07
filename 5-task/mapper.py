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
            print "{0}\t{1}\t{2}".format( j['product/title'], j['review/score'],j['review/time'])
        except Exception as e: 
            continue
