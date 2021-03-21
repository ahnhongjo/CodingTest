import sys

num=int(input())
answer=0
pos=1
while num!=0:
    answer+=(num%10)//3*pos
    num=num//10
    if num==0:
        break

    answer+=num*3*pos
    pos*=10

print(answer)




