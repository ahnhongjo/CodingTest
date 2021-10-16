import math

def solution(n, k):
    change_num = change(n,k)
    answer = 0
    tmp_num = ""
    for i in change_num:
        if i=="0" and tmp_num!="":
            if isprime(int(tmp_num)):
                answer+=1
            tmp_num=""
        else:
            tmp_num=tmp_num+i

    if isprime(int(tmp_num)):
        answer += 1

    return answer

def change(n,k):
    return_str=""
    while n!=0:
        return_str=str(n%k)+return_str
        n=n//k

    return return_str

def isprime(n):
    if n==1 or n==0:
        return False
    for i in range(2,math.ceil(math.sqrt(n+1))):
        if n%i==0:
            return False
    return True

solution(437674,3)