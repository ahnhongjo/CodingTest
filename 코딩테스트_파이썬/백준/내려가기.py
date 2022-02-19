def sol():
    num = int(input())
    max_dp = []
    min_dp = []

    a,b,c = list(map(int, input().split()))
    max_dp.append(a)
    max_dp.append(b)
    max_dp.append(c)
    min_dp.append(a)
    min_dp.append(b)
    min_dp.append(c)

    for i in range(1, num):
        x1, x2, x3 = map(int, input().split())
        max_x1 = x1+max(max_dp[0],max_dp[1])
        max_x2 = x2 + max(max_dp)
        max_x3 = x3 + max(max_dp[2], max_dp[1])

        max_dp[0]=max_x1
        max_dp[1]=max_x2
        max_dp[2]=max_x3

        min_x1=x1+min(min_dp[0],min_dp[1])
        min_x2 = x2 + min(min_dp)
        min_x3 = x3 + min(min_dp[2], min_dp[1])

        min_dp[0]=min_x1
        min_dp[1]=min_x2
        min_dp[2]=min_x3

    print(max(max_dp),min(min_dp))
sol()
