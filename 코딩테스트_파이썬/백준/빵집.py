import copy
from collections import deque

def sol():
    r, c = map(int, input().split())
    building = []
    ans = 0
    for _ in range(r):
        building.append(list(input()))

    for i in range(r):
        start = (i, 0)
        ans += check_road(start, building, r, c)

    print(ans)


def check_road(start, building, r, c):
    road = [start]
    queue = deque()
    queue.append((start, road))
    dirs = [(1, 1), (0, 1), (-1, 1)]

    while queue:
        tmp = queue.pop()
        nownode = tmp[0]

        for dir in dirs:
            move_node = (nownode[0] + dir[0], nownode[1] + dir[1])
            if move_node[0] < 0 or move_node[0] >= r or move_node[1] < 0 or move_node[1] >= c:
                continue
            if building[move_node[0]][move_node[1]] == 'x':
                continue

            tmp_road = copy.deepcopy(tmp[1])
            tmp_road.append(move_node)
            if move_node[1] == c-1:
                for i in tmp_road:
                    building[i[0]][i[1]] = 'x'
                return 1
            queue.append((move_node, tmp_road))

    return 0


sol()
