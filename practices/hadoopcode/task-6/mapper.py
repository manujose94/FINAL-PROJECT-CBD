#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split(" ") #Split by single space
    if len(data) == 10:
        ip, idclient, iduser, date, date2, typereq, item, protocol, codestate, size = data
        print "{0}\t{1}".format(item,typereq)

