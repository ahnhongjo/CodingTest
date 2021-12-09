def sol():
    c, n = map(int,input().split())
    dp=[int(1e9)]*100001
    dp[0] = 0
    for _ in range(n):
        cost, customer = map(int,input().split())
        for i in range(100000-customer+1):
            if dp[i]+cost<dp[i+customer]:
                dp[i+customer] =dp[i]+cost

    print(min(dp[c:]))

sol()