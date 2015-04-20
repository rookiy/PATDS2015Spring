#!/usr/bin/env python
import sys

tree = []
ans = []

def findroot(l):
    N = len(l)
    Nodeindex = [str(i) for i in range(N)]
    for node in l:
        if node[0] in Nodeindex:
            Nodeindex.remove(node[0])
        if node[1] in Nodeindex:
            Nodeindex.remove(node[1])
    return int(Nodeindex[0])

def visit(index):
    if tree[index][0] == '-' and tree[index][1] == '-':
        ans.append(str(index))

def Traverse(root):
    stack = []
    stack.append(root)
    while len(stack) > 0:
        current = stack.pop(0)
        visit(current)
        if tree[current][0] != '-':
            left = int(tree[current][0])
            stack.append(left)
        if tree[current][1] != '-':
            right = int(tree[current][1])
            stack.append(right)

'''
def MidTraverse(root):
    if tree[root][0] != '-':
        left = int(tree[root][0])
        Traverse(left)
    visit(root)
    if tree[root][1] != '-':
        right = int(tree[root][1])
        Traverse(right)
'''    
def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    for i in range(N):
        tree.append(raw_input().split())
    root = findroot(tree)
    Traverse(root)
    print ' '.join(ans)
    
    
if __name__ == '__main__':
    main()
