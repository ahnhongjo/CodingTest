from collections import deque

def sol():
    n, m = map(int, input().split())
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    road = []
    dp =[[0 for i in range(m)]for j in range(n)]

    for _ in range(n):
        tmp = list(map(int, input().split()))
        road.append(tmp)

    q = deque()
    q.append((0, 0))

    while q:
        now = q.pop()
        dp[now[0]][now[1]]+=1

        now_road = road[now[0]][now[1]]
        tmp = []
        for dir in dirs:

            x = now[0] + dir[0]
            y = now[1] + dir[1]

            if x >= n or x < 0 or y >= m or y < 0:
                continue
            after_road = road[x][y]
            if now_road > after_road:
                tmp.append((after_road,x,y))

        tmp.sort()
        for i in tmp:
            q.append((i[1],i[2]))

    for i in dp:
        print(i)
    print(dp[-1][-1])
sol()