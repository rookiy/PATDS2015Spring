#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    numstr = raw_input()
    n = int(numstr)
    m = n * 2
    doublestr = str(m)
    l1 = list(numstr)
    l1.sort()
    l2 = list(doublestr)
    l2.sort()
    if l1 == l2:
        print 'Yes'
    else:
        print 'No'
    print m
    

if __name__ == '__main__':
    main()
