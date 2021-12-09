from itertools import combinations

def sol():
    num = int(input())
    for i in range(num):
        n, m = map(int,input().split())
        print(facto(m)//(facto(n)*facto(m-n)))

def facto(n):
    result = 1
    for i in range(1,n+1):
        result *=i

    return result


sol()