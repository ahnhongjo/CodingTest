from itertools import combinations
import copy


def sol():
    n = int(input())
    hall = []
    empty = []
    student = []
    i = 0
    j = 0

    for _ in range(n):
        tmp = list(input().split())
        j = 0
        for a in tmp:
            if a == 'X':
                empty.append((i, j))
            elif a == 'S':
                student.append((i, j))
            j += 1
        i += 1
        hall.append(tmp)

    for i in list(combinations(empty, 3)):
        if check(hall, i, student, n):
            print("YES")
            return

    print("NO")
    return


def check(hall, obstacle, student, n):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    tmp_hall = copy.deepcopy(hall)
    for o in obstacle:
        tmp_hall[o[0]][o[1]] = 'O'
    for s in student:
        for dir in dirs:
            s_x = s[0]
            s_y = s[1]
            while True:
                s_x += dir[0]
                s_y += dir[1]
                if s_x < 0 or s_x >= n or s_y < 0 or s_y >= n:
                    break
                if tmp_hall[s_x][s_y] == 'T':
                    return False
                elif tmp_hall[s_x][s_y] == 'O':
                    break
    return True


sol()
