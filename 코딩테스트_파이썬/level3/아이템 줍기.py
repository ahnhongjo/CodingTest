from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    min_x = 50
    max_x = 0
    min_y = 50
    max_y = 0
    border = []
    answerelist = []

    for i in rectangle:
        if i[0] < min_x:
            min_x = i[0]
        if i[2] > max_x:
            max_x = i[2]
        if i[1] < min_y:
            min_y = i[1]
        if i[3] > max_y:
            max_y = i[3]

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if rectangle_border((i, j), rectangle):
                border.append((i, j))

    q = deque()

    q.append((characterX, characterY, 0))
    visited = set()

    visited.add((characterX, characterY))

    while q:
        now = q.popleft()
        if now[0] == itemX and now[1] == itemY:
            answerelist.append(now[2])
        for dir in dirs:
            if (now[0] + dir[0], now[1] + dir[1]) in border and (now[0] + dir[0], now[1] + dir[1]) not in visited:
                if not rectangle_border((now[0] + dir[0] / 2, now[1] + dir[1] / 2), rectangle):
                    continue
                q.append((now[0] + dir[0], now[1] + dir[1], now[2] + 1))
                visited.add((now[0] + dir[0], now[1] + dir[1]))

    answer = min(answerelist)
    print(answer)

    return answer


def rectangle_border(grid, rectangle):
    x = grid[0]
    y = grid[1]
    border = False
    for i in rectangle:
        if x == i[0] and y >= i[1] and y <= i[3]:
            border = True
            continue
        if x == i[2] and y >= i[1] and y <= i[3]:
            border = True
            continue
        if y == i[1] and x >= i[0] and x <= i[2]:
            border = True
            continue
        if y == i[3] and x >= i[0] and x <= i[2]:
            border = True
            continue

        if x > i[0] and x < i[2] and y > i[1] and y < i[3]:
            return False

    return border


solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
