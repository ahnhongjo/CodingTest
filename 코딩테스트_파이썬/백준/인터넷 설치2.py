from collections import deque
import copy

def sol():
    n, p, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    maxCost = 0

    for _ in range(p):
        pc1, pc2, cost = map(int, input().split())
        if maxCost < cost:
            maxCost = cost
        graph[pc1].append([pc2, cost])
        graph[pc2].append([pc1, cost])

    start = 0
    end = maxCost

    res = -1

    while start <= end:
        mid = (start+end)//2

        if connect_check(graph,k,mid,n):
            res = mid
            end = mid-1
        else:
            start = mid+1

    print(res)


def connect_check(graph, k, maxCost,n):
    q = deque()
    visited = set()
    visited.add(1)
    q.append((1, k, visited))

    while q:
        now_node = q.popleft()
        if now_node[0] == n:
            return True

        for i in graph[now_node[0]]:
            if i[0] in now_node[2]:
                continue

            tmp_k = now_node[1]
            if i[1] > maxCost:
                if now_node[1] == 0:
                    continue
                else:
                    tmp_k -= 1
            tmp_visited = copy.deepcopy(now_node[2])
            tmp_visited.add(i[0])

            q.append((i[0],tmp_k,tmp_visited))

    return False

sol()

