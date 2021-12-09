import math
from itertools import combinations

def sol():
    nums=[9,8,7,6,5,4,3,2,1,0]
    n = int(input())
    if n > 1023:
        print(-1)
        return

    for i in range(1,11):
        now_num = comb(i)
        if n <=now_num:
            break
        else:
            n -= now_num
    numlist=list(combinations(nums,i))
    numlist.sort()
    ans=numlist[n-1]
    answer=0
    for i in ans:
        answer =answer*10+i
    print(answer)

def comb(r):
    return math.factorial(10)//(math.factorial(10-r)*math.factorial(r))

sol()