def solution(land):
    num = len(land)

    dp = [[0 for i in range(num)] for j in range(num)]
    pos = [[0 for i in range(num)] for j in range(num)]

    for i in range(num):
        tmp=max(land[i])
        dp[i][i] = tmp
        pos[i][i] = (land[i].index(tmp),land[i].index(tmp))

    for dif in range(1, num):
        for start in range(num - dif):
            sum_value = []
            tmp_pos = []
            for k in range(start, start + dif + 1):
                max_value = 0
                max_pos = 0
                if k == start:
                    for x in range(4):
                        if x == pos[k + 1][start + dif][0]:
                            continue
                        if max_value < land[k][x]:
                            max_value = land[k][x]
                            max_pos = x
                    sum_value.append(max_value + dp[k + 1][start + dif])
                    tmp_pos.append((max_pos, pos[k + 1][start + dif][1]))
                elif k == start + dif:
                    for x in range(4):
                        if x == pos[start][k - 1][1]:
                            continue
                        if max_value < land[k][x]:
                            max_value = land[k][x]
                            max_pos = x
                    sum_value.append(max_value + dp[start][k - 1])
                    tmp_pos.append((pos[start][k-1][0],max_pos))
                else:
                    for x in range(4):
                        if x == pos[start][k - 1][1] or x == pos[k + 1][start + dif][0]:
                            continue
                        if max_value < land[k][x]:
                            max_value = land[k][x]
                            max_pos = x
                    sum_value.append(max_value + dp[start][k - 1] + dp[k + 1][start + dif])
                    tmp_pos.append((pos[start][k-1][0],pos[k+1][start+dif][1]))

            dp[start][start+dif]=max(sum_value)
            pos[start][start+dif]=tmp_pos[sum_value.index(max(sum_value))]


    for x in dp:
        print(x)
    return dp[0][num-1]


print(solution([[3,4,5,6],[7,9,10,5],[8,9,10,11],[1,4,5,12],[1,2,3,4]]))
