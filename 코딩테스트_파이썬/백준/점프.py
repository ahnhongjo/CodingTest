from collections import deque


def sol():
    n = int(input())
    board = []
    dp = [[0 for i in range(n)]for j in range(n)]

    for i in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)

    x = board[0][0]
    dp[x][0] =1
    dp[0][x]=1

    for i in range(n):
        for j in range(n):
            if i==n-1 and j ==n-1:
                continue
            tmp = board[i][j]
            if i+tmp <n:
                dp[i+tmp][j] +=dp[i][j]
            if j+tmp<n:
                dp[i][j+tmp] += dp[i][j]
    print(dp[n-1][n-1])
sol()
