def sol():
    n,k=map(int,input().split())

    money=[]
    for i in range(n):
        money.append(int(input()))

    money_num=0
    remain_money=k

    for i in range(n-1,-1,-1):
        tmp_money=remain_money//money[i]
        money_num+=tmp_money
        remain_money-=tmp_money*money[i]

    print(money_num)

sol()