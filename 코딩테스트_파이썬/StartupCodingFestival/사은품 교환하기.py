def solution():
    user_input = int(input())
    answer_list = []

    for i in range(user_input):
        n, m = map(int, input().split())
        answer_list.append(gift_num(n, m))

    for i in answer_list:
        print(i)

def gift_num(n,m):
    ndiv5=n//5
    mdiv7=m//7

    num=min(ndiv5,mdiv7)

    rem_n=n-5*num
    rem_m=m-7*num

    if rem_n<5 or rem_n+rem_m<12:
        return num
    else:
        return num+(rem_n+rem_m)//12

solution()