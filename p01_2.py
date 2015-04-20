#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    l = map(int, raw_input().split())
    
    # start from a positive integer
    for i in range(N):
        if l[i] >= 0:
            break
    # record largest sum, note that initial maxsum is -1, for there may be
    # a case like -1 0 -2, you should record 0's number in loop 
    maxsum = -1
    start = l[0]
    end = l[N-1]
    # record current sum, if positive then continue, else start from now
    tmpsum = 0
    j = i
    while j < N:
        tmpsum = tmpsum + l[j]
        if tmpsum > maxsum:
            maxsum = tmpsum
            start = l[i]
            end = l[j]
        j += 1
        if tmpsum <= 0:
            i = j
            tmpsum = 0
    # if every number is negative, then print 0 
    if maxsum < 0:
        maxsum = 0
    print str(maxsum)+' '+str(start)+' '+str(end) 
        
if __name__ == '__main__':
    main()