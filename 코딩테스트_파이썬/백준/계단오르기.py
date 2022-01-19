def sol():
    n = int(input())
    stairs=[]
    dp=[]

    for _ in range(n):
        stairs.append(int(input()))
    if n==1:
        print(stairs[0])
        return
    dp.append([stairs[0],stairs[1]])
    dp.append([0,stairs[0]+stairs[1]])

    for i in range(2,n):
        dp[0].append(max(dp[0][i-2]+stairs[i],dp[1][i-2]+stairs[i]))
        dp[1].append(dp[0][i-1]+stairs[i])

    print(max(dp[0][-1],dp[1][-1]))

sol()