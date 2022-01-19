def solution(m, n, board):
    answer = 0
    bomb_num=0
    tmpboard = []

    for i in range(m):
        tmpboard.append(list(board[i]))

    while True:
        bomb = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if tmpboard[i][j] != 0 and (
                        tmpboard[i][j] == tmpboard[i + 1][j] == tmpboard[i][j + 1] == tmpboard[i + 1][j + 1]):
                    bomb.add((i, j))
                    bomb.add((i + 1, j))
                    bomb.add((i, j + 1))
                    bomb.add((i + 1, j + 1))

        if len(bomb) == 0:
            break

        for i, j in bomb:
            tmpboard[i][j] = 0
            bomb_num+=1

        for j in range(n):
            for i in range(m):
                if tmpboard[i][j] == 0:
                    for a in range(i, 0, -1):
                        tmp = tmpboard[a][j]
                        tmpboard[a][j] = tmpboard[a - 1][j]
                        tmpboard[a - 1][j] = tmp

    return m*n-bomb_num


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
