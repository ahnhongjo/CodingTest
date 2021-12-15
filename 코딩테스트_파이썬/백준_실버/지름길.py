import heapq


def sol():
    n, d = map(int, input().split())
    ans = d
    end_node=set()
    fast_road=[]
    distance={}

    for _ in range(n):
        s, e, zd = map(int, input().split())
        if e>d or e-s<=zd:
            continue
        fast_road.append((s,e,zd))

    fast_road.sort(key=lambda x:x[1])

    for i in fast_road:
        s, e, zd = i
        tmp_short=s+zd
        for j in end_node:
            if s < j:
                continue
            if distance[j] + (s-j) + zd <tmp_short:
                tmp_short = distance[j] + (s-j) + zd

        if not e in end_node:
            end_node.add(e)
            distance[e] = tmp_short
        else:
            if distance[e] >tmp_short:
                distance[e]=tmp_short

    for i in end_node:
        if distance[i]+(d-i) <ans:
            ans = distance[i]+(d-i)

    print(ans)

sol()