from collections import deque


def sol():
    n, m = map(int, input().split())
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    cheese = []

    for _ in range(n):
        cheese.append(list(map(int, input().split())))

    outair(cheese, (0, 0), n, m)

    time = 0

    while True:
        melt_cheese = []
        for i in range(n):
            for j in range(m):
                if cheese[i][j] == 1:
                    air = 0
                    for dir in dirs:
                        if cheese[i + dir[0]][j + dir[1]] == 2:
                            air += 1

                    if air >= 2:
                        melt_cheese.append((i, j))

        if len(melt_cheese) == 0:
            break
        for i in melt_cheese:
            outair(cheese, i, n, m)
        time += 1

    print(time)


def outair(cheese, start, n, m):
    q = deque()
    q.append(start)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        now = q.pop()
        cheese[now[0]][now[1]] = 2

        for dir in dirs:
            move = (now[0] + dir[0], now[1] + dir[1])
            if move[0] < 0 or move[0] >= n or move[1] < 0 or move[1] >= m:
                continue
            if cheese[move[0]][move[1]] == 1:
                continue
            if cheese[move[0]][move[1]] == 2:
                continue

            q.append(move)


sol()
