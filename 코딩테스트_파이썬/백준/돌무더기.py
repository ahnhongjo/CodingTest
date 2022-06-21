import sys

def sol():
    input = sys.stdin.readline
    n = int(input())

    for i in range(n):
        x, y, z = map(int,input().split())
        even_num = 0
        if x & 1 == 0:
            even_num += 1
        if y & 1 == 0:
            even_num += 1
        if z & 1 == 0:
            even_num += 1
        if even_num == 2 or even_num == 3:
            print("R")
        else:
            print("B")


sol()
