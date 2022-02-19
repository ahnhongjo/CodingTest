def solution(board, skill):
    row = len(board)
    col = len(board[0])
    answer = 0

    ac_sum=[[0]*(col+1) for i in range(row+1)]

    for sk in skill:
        if sk[0] ==1:
            ac_sum[sk[1]][sk[2]] -= sk[5]
            ac_sum[sk[1]][sk[4]+1] +=sk[5]
            ac_sum[sk[3]+1][sk[2]] +=sk[5]
            ac_sum[sk[3]+1][sk[4]+1] -=sk[5]
        else:
            ac_sum[sk[1]][sk[2]] += sk[5]
            ac_sum[sk[1]][sk[4]+1] -=sk[5]
            ac_sum[sk[3]+1][sk[2]] -=sk[5]
            ac_sum[sk[3]+1][sk[4]+1] +=sk[5]

    for i in range(row):
        for j in range(col+1):
            ac_sum[i+1][j] +=ac_sum[i][j]

    for j in range(col):
        for i in range(row+1):
            ac_sum[i][j+1] +=ac_sum[i][j]

    for i in range(row):
        for j in range(col):
            if board[i][j]+ac_sum[i][j]>0:
                answer+=1

    return answer


solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
         [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])
