from collections import deque


def sol():
    n, k, r = map(int, input().split())
    farm = [[0 for i in range(n + 1)] for j in range(n + 1)]
    cowlist = []
    ans = 0

    road = set()

    for _ in range(r):
        tmproad = list(input().split())
        # A -> B로 가는 길
        road.add("".join(tmproad))
        tmproad = tmproad[2:] + tmproad[:2]
        # B -> A로 가는 길
        road.add("".join(tmproad))

    for _ in range(k):
        a, c = map(int, input().split())
        farm[a][c] = 1
        cowlist.append((a, c))

    for i in cowlist:
        q = deque()
        q.append(i)
        visited = set()
        visited.add(i)

        while q:
            nownode = q.popleft()

            # 경계체크
            if nownode[0] - 1 > 0:
                tmpstr = str(nownode[0]) + str(nownode[1]) + str(nownode[0] - 1) + str(nownode[1])
                tmptuple = (nownode[0] - 1, nownode[1])

                # 길을 지나는지의 여부, 이미 방문한 노드인지 확인
                if tmpstr not in road and tmptuple not in visited:
                    visited.add(tmptuple)

                    # 소를 만났을경우
                    if farm[nownode[0] - 1][nownode[1]] == 1:
                        ans += 1
                    q.append(tmptuple)

            if nownode[0] + 1 <= n:
                tmpstr = str(nownode[0]) + str(nownode[1]) + str(nownode[0] + 1) + str(nownode[1])
                tmptuple = (nownode[0] + 1, nownode[1])
                if tmpstr not in road and tmptuple not in visited:
                    visited.add(tmptuple)
                    if farm[nownode[0] + 1][nownode[1]] == 1:
                        ans += 1
                    q.append(tmptuple)

            if nownode[1] - 1 > 0:
                tmpstr = str(nownode[0]) + str(nownode[1]) + str(nownode[0]) + str(nownode[1] - 1)
                tmptuple = (nownode[0], nownode[1] - 1)
                if tmpstr not in road and tmptuple not in visited:
                    visited.add(tmptuple)
                    if farm[nownode[0]][nownode[1] - 1] == 1:
                        ans += 1
                    q.append(tmptuple)

            if nownode[1] + 1 <= n:
                tmpstr = str(nownode[0]) + str(nownode[1]) + str(nownode[0]) + str(nownode[1] + 1)
                tmptuple = (nownode[0], nownode[1] + 1)
                if tmpstr not in road and tmptuple not in visited:
                    visited.add(tmptuple)
                    if farm[nownode[0]][nownode[1] + 1] == 1:
                        ans += 1
                    q.append(tmptuple)

    # 전체 경우의 수 kC2에서 만난 쌍의 수를 뺌
    print((k * (k - 1) - ans) // 2)


sol()

