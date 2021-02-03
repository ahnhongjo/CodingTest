def solution(triangle):
    num = len(triangle)

    dp = [[0 for i in range(num)] for j in range(num)]

    dp[0][0] = triangle[0][0]

    for i in range(1, num):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    answer = max(dp[num - 1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
