#!/usr/bin/python
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")
        if len(data) != 10:
            continue
            
        ip, identity, usrname, time, zone, method, path, protocol, status, size = data
        if path[:17] == 'http://www.the-as':
            path = path[31:]
        
        print("{0}".format(ip))

def main():
    import StringIO
    mapper()
    sys.stdin = sys.__stdin__

main()