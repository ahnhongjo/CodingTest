
def sol():
    n, k = map(int, input().split())
    dp=[i for i in range(n+1,0,-1)]
    if k==1:
        print(1)
        return
    if k==2:
        print(n+1)
        return
    for i in range(k-3):
        for j in range(n):
            dp[j] = sum(dp[j:])%1000000000

    print(sum(dp)%1000000000)

sol()
