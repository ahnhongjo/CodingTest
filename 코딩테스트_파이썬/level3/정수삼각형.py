def solution(triangle):
    n = len(triangle)

    dp = [[0 for i in range(n)] for j in range(n)]
    pos = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        tmp = max(triangle[i])
        dp[i][i] = tmp
        pos[i][i] = (triangle[i].index(tmp), triangle[i].index(tmp))

    for i in dp:
        for j in i:
            print(j, end=" ")
        print()

    for i in pos:
        for j in i:
            print(j, end="    ")
        print()

    for i in range(1, n):
        for x in range(n - i):
            tmp = []
            tmp.append(dp[x][x+i-1] + triangle[x+1][pos[x][1]])
            tmp.append(dp[x][x+i-1] + triangle[x+1][pos[x][1]+1])
            tmp.append(dp[x+1][x+i]+triangle[x][pos[x+1][0]-1])
            tmp.append(dp[x + 1][x + i] + triangle[x][pos[x + 1][0]])

    answer = 0
    return answer


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
