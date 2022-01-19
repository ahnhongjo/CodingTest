from collections import deque
import sys

input = sys.stdin.readline

def sol():
    n, m = map(int, input().split())
    farm = [[0] * (n + 1) for i in range(n + 1)]
    visited = [[0] * (n + 1) for i in range(n + 1)]
    farm[1][1] = 1
    visited[1][1] = 1
    switch = {}

    for _ in range(m):
        i, j, k, l = map(int, input().split())

        if (i, j) in switch:
            switch[(i, j)].append((k, l))
        else:
            switch[(i, j)] = [(k, l)]

    q = deque()
    q.append((1, 1))

    ans = 0

    while q:
        now = q.popleft()
        ans += 1
        if now in switch:
            for i in switch[now]:
                if farm[i[0]][i[1]] == 0:
                    farm[i[0]][i[1]] = 1
            bfs(farm, visited, n, q)
        else:
            continue

    print(ans)


def bfs(farm, visited, n, queue):
    q = deque()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q.append((1, 1))
    tmpvisited=set()

    while q:
        now = q.popleft()
        for dir in dirs:
            move = (now[0] + dir[0], now[1] + dir[1])
            if move[0] <= 0 or move[0] > n or move[1] <= 0 or move[1] > n:
                continue
            if farm[move[0]][move[1]] == 0:
                continue
            if visited[move[0]][move[1]] == 0:
                visited[move[0]][move[1]] = 1
                queue.append((move[0], move[1]))
            if move not in tmpvisited:
                tmpvisited.add(move)
                q.append(move)


sol()
