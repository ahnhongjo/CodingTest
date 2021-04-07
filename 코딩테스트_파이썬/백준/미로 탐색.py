from queue import PriorityQueue

def sol():
    n, m = map(int, input().split())

    mirror = []
    for i in range(n):
        tmp = []
        tmp_string = input()
        for j in range(m):
            tmp.append(int(tmp_string[j]))
        mirror.append(tmp)

    for i in mirror:
        print(i)

    que = PriorityQueue()
    que.put((n + m - 2, (0, 0), mirror, 1))

    while not que.empty():
        tmp = que.get()

        pos = tmp[1]
        tmp_map = tmp[2]
        length = tmp[3]

        if pos[0] == n - 1 and pos[1] == m - 1:
            print(tmp[3])
            return

        if pos[0] - 1 >= 0 and mirror[pos[0] - 1][pos[1]] == 1:
            que.put(move(pos[0] - 1, pos[1], tmp_map, length))

        if pos[1] - 1 >= 0 and mirror[pos[0]][pos[1] - 1] == 1:
            que.put(move(pos[0], pos[1] - 1, tmp_map, length))

        if pos[0] + 1 <= n - 1 and mirror[pos[0] + 1][pos[1]] == 1:
            que.put(move(pos[0] + 1, pos[1], tmp_map, length))

        if pos[1] + 1 <= m - 1 and mirror[pos[0]][pos[1] + 1] == 1:
            que.put(move(pos[0], pos[1] + 1, tmp_map, length))


def move(i, j, maps, length):
    n = len(maps)
    m = len(maps[0])
    maps[i][j] = 0
    return n + m - i - j + length, (i, j), maps, length + 1

sol()
