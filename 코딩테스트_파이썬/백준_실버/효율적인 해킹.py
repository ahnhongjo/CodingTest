import copy
import sys

input=sys.stdin.readline

def sol():
    m,n = map(int,input().split())

    hacker = [set() for _ in range(m+1)]
    child_num=[0 for _ in range(m+1)]
    max_child=0
    for i in range(n):
        c,p = map(int,input().split())
        hacker[p].add(c)
    for i in range(1,m+1):
        child_set = set()


sol()