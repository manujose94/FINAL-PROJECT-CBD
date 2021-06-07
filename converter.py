#!/usr/bin/python2
import gzip
import json

def parse(filename):
  f = gzip.open(filename, 'r')
  entry = {}
  for l in f:
    l = l.strip()
    colonPos = l.find(':')
    if colonPos == -1:
      yield entry
      entry = {}
      continue
    eName = l[:colonPos]
    rest = l[colonPos+2:]
    entry[eName] = rest
  yield entry

target = open("Video_Games.json", 'w+')
for e in parse("Video_Games.txt.gz"):
  target.writelines(json.dumps(e)+'\n')
target.close() 

