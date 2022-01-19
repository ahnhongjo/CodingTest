def sol():
    num = int(input())
    if num%2 ==1:
        print(0)
        return
    dp =[3]

    for i in range(num//2-1):
        tmp =0
        for j in range(i+1):
            if j ==i:
                tmp+=dp[j]*3
            else:
                tmp+=dp[j]*2
        dp.append(tmp+2)

    print(dp[-1])

sol()