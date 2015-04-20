#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    l = map(int, raw_input().split())
    
    # start from a positive integer
    for i in range(N):
        if l[i] > 0:
            break
    # record largest sum
    maxsum = 0
    # record current sum, if positive then continue, else start from now
    tmpsum = 0
    j = i
    while j < N:
        tmpsum = tmpsum + l[j]
        if tmpsum > maxsum:
            maxsum = tmpsum
        j += 1
        if tmpsum <= 0:
            i = j
            tmpsum = 0
    
    print maxsum
        
if __name__ == '__main__':
    main()