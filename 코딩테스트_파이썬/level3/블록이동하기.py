from collections import deque


def solution(board):
    answer = 0
    n = len(board)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()

    q = deque()
    q.append(((0, 0), (0, 1), 0))
    visited.add(((0,0),(0,1)))

    while q:
        now = q.popleft()
        if now[0] == (n - 1, n - 1) or now[1] == (n - 1, n - 1):
            return now[2]
        p1 = now[0]
        p2 = now[1]
        sec = now[2]

        for dir in dirs:
            dir_x = p1[0] + dir[0]
            dir_y = p1[1] + dir[1]
            if dir_x >= n or dir_x < 0 or dir_y >= n or dir_y < 0 or board[dir_x][dir_y] == 1:
                continue
            dir_x2 = p2[0] + dir[0]
            dir_y2 = p2[1] + dir[1]
            if dir_x2 >= n or dir_x2 < 0 or dir_y2 >= n or dir_y2 < 0 or board[dir_x2][dir_y2] == 1:
                continue
            if ((dir_x, dir_y), (dir_x2, dir_y2)) in visited or ((dir_x2, dir_y2), (dir_x, dir_y)) in visited:
                continue
            q.append(((dir_x, dir_y), (dir_x2, dir_y2), sec + 1))
            visited.add(((dir_x, dir_y), (dir_x2, dir_y2)))

        rots = can_rotate(p1, p2, board, visited)

        for rot in rots:
            q.append((rot[0], rot[1], sec + 1))
            visited.add((rot[0],rot[1]))
    return answer


def can_rotate(p1, p2, board, visited):
    n = len(board)
    res = []

    # 수직
    if p1[0] == p2[0]:
        if p1[0] - 1 >= 0 and board[p1[0] - 1][p1[1]] == 0 and board[p2[0] - 1][p2[1]] == 0:
            if (p1, (p1[0] - 1, p1[1])) not in visited and ((p1[0] - 1, p1[1]), p1) not in visited:
                res.append((p1, (p1[0] - 1, p1[1])))
        if p1[0] + 1 < n and board[p1[0] + 1][p1[1]] == 0 and board[p2[0] + 1][p2[1]] == 0:
            if (p1, (p1[0] + 1, p1[1])) not in visited and ((p1[0] + 1, p1[1]), p1) not in visited:
                res.append((p1, (p1[0] + 1, p1[1])))
        if p2[0] - 1 >= 0 and board[p2[0] - 1][p2[1]] == 0 and board[p1[0] - 1][p1[1]] == 0:
            if ((p2[0] - 1, p2[1]), p2) not in visited and (p2, (p2[0] - 1, p2[1])) not in visited:
                res.append(((p2[0] - 1, p2[1]), p2))
        if p2[0] + 1 < n and board[p2[0] + 1][p2[1]] == 0 and board[p1[0] + 1][p1[1]] == 0:
            if ((p2[0] + 1, p2[1]), p2) not in visited and (p2, (p2[0] + 1, p2[1])) not in visited:
                res.append(((p2[0] + 1, p2[1]), p2))

        return res

    # 수평
    elif p1[1] == p2[1]:
        if p1[1] - 1 >= 0 and board[p1[0]][p1[1] - 1] == 0 and board[p2[0]][p2[1] - 1] == 0:
            if (p1, (p1[0], p1[1] - 1)) not in visited and ((p1[0], p1[1] - 1), p1) not in visited:
                res.append(((p1[0], p1[1] - 1), p1))
        if p1[1] + 1 < n and board[p1[0]][p1[1] + 1] == 0 and board[p2[0]][p2[1] + 1] == 0:
            if (p1, (p1[0], p1[1] + 1)) not in visited and ((p1[0], p1[1] + 1), p1) not in visited:
                res.append(((p1[0], p1[1] + 1), p1))
        if p2[1] - 1 >= 0 and board[p2[0]][p2[1] - 1] == 0 and board[p1[0]][p1[1] - 1] == 0:
            if (p2, (p2[0], p2[1] - 1)) not in visited and ((p2[0], p2[1] - 1), p2) not in visited:
                res.append(((p2[0], p2[1] - 1), p2))
        if p2[1] + 1 < n and board[p2[0]][p2[1] + 1] == 0 and board[p1[0]][p1[1] + 1] == 0:
            if (p2, (p2[0], p2[1] + 1)) not in visited and ((p2[0], p2[1] + 1), p2) not in visited:
                res.append((p2, (p2[0], p2[1] + 1)))

        return res


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
