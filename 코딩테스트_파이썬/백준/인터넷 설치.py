from collections import deque
import copy
import sys
input = sys.stdin.readline

def sol():
    n, p, k = map(int,input().split())
    graph = [[]for _ in range(n+1)]
    ans = int(1e9)
    connected = False

    for i in range(p):
        pc1, pc2, cost = map(int,input().split())
        graph[pc1].append([pc2, cost])
        graph[pc2].append([pc1,cost])

    q=deque()
    visited = set()
    visited.add(1)

    q.append((1,[0],visited))

    while q:
        nownode=q.pop()

        if n in nownode[2]:
            connected = True
            cost = nownode[1]
            cost.sort(reverse=True)
            if cost[k]<ans:
                ans=cost[k]
            continue

        for i in graph[nownode[0]]:
            if i[0] in nownode[2]:
                continue
            else:
                tmpvisited = copy.deepcopy(nownode[2])
                tmpvisited.add(i[0])
                tmpcost=copy.deepcopy(nownode[1])
                tmpcost.append(i[1])
                q.append((i[0],tmpcost,tmpvisited))

    if connected:
        print(ans)
    else:
        print(-1)
sol()