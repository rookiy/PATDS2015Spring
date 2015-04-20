#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    M, N, K = map(int, raw_input().split())
    for i in range(K):
        flag = True
        empty = True
        stack = []
        l = [i for i in range(1, N+1)]
        out = map(int, raw_input().split())
        for j in out:
            index = l.index(j)
            # stack not empty, pop the top element or higher element
            if not empty :
                if index <= topindex and top != j:
                    flag = False
                    break
            # pop current to see if stack get empty
            if index != 0:
                empty = False
                top = l[index-1]
                topindex = index-1
            else:
                empty = True
            if index+1 > M:
                flag = False
                break
            l.remove(j)
            
        if flag:
            print 'YES'
        else:
            print 'NO'
    
if __name__ == '__main__':
    main()
