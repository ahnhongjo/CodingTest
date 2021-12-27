from collections import deque
import copy

def sol():
    n,k = map(int,input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int,input().split())))

    for m in range(n):
        for s in range(n):
            for e in range(n):
                graph[s][e] = min(graph[s][e],graph[s][m]+graph[m][e])

    q = deque()
    visited = set()
    visited.add(k)
    cost = 0
    result = int(1e9)

    q.append((k,visited,cost))

    while q:
        nownode = q.popleft()
        nownum = nownode[0]
        if len(nownode[1]) == n:
            result = min(result,nownode[2])
            continue

        for i in range(n):
            if i in nownode[1]:
                continue
            tmp_cost = nownode[2]+graph[nownum][i]
            tmp_visited = copy.deepcopy(nownode[1])
            tmp_visited.add(i)
            if tmp_cost > result:
                continue
            q.append((i,tmp_visited,tmp_cost))

    print(result)

sol()