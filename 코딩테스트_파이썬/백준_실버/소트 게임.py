from collections import deque
import sys

input = sys.stdin.readline
def sol():
    n, k = map(int,input().split())
    perm = "".join(input().split())
    visited=[]

    make=""
    for i in range(1,n+1):
        make+=str(i)
    if make == perm:
        print(0)
        return
    perm_cand=deque()
    perm_cand.append(perm)
    num = 1
    while perm_cand:
        length=len(perm_cand)
        for _ in range(length):
            tmp = perm_cand.popleft()
            for i in range(n - k + 1):
                tmp_reverse = reverse(tmp, i, k)
                if tmp_reverse == make:
                    print(num)
                    return
                elif not tmp_reverse in visited:
                    perm_cand.append(tmp_reverse)
                    visited.append(tmp_reverse)
        num+=1
    print(-1)

def reverse(num_list,pos,k):
    reverse_tmp=list(num_list)
    for i in range(k//2):
        tmp = reverse_tmp[pos+i]
        reverse_tmp[pos+i]=reverse_tmp[pos+k-1-i]
        reverse_tmp[pos + k - 1 - i] = tmp
    return "".join(reverse_tmp)


sol()