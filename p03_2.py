#!/usr/bin/env python
import sys
import re

Pattern = re.compile(r'Push (\d*)')
ans = []
tree = {}
stack = []

def visit(node):
    ans.append(node)

def postorder(node):
    if tree[node][0] != '-1':
        postorder(tree[node][0])
    if tree[node][1] != '-1':
        postorder(tree[node][1])
    visit(node)

def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    # push root node in stack
    match = Pattern.match(raw_input())
    current = match.group(1)
    root = current
    tree[current] = ['-1', '-1']
    stack.append(current)
    pre = current
    lr = 0
    # build the tree
    for i in range(1, 2*N):
        match = Pattern.match(raw_input())
        if match:
            current = match.group(1)
            tree[pre][lr] = current
            tree[current] = ['-1', '-1']
            stack.append(current)
            pre = current
            lr = 0
        else:
            pre = stack.pop()
            lr = 1
    # postorder traverse
    postorder(root)
    print ' '.join(ans)

if __name__ == '__main__':
    main()
