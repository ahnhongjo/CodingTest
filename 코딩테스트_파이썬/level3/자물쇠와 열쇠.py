def solution(key, lock):
    key_1 = []
    lock_0 = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key_1.append((i, j))

    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lock_0.append((i, j))
    if len(lock_0)==0:
        return True

    lock_0.sort(key=lambda x: (x[1], x[0]))

    for i in range(4):
        key_1 = rotate90(key_1)
        for j in range(4):

            key_1.sort(key=lambda x: (x[j//2], x[j%2]))

            key_1_trans = trans(key_1, lock_0[0][0] - key_1[0][0], lock_0[0][1] - key_1[0][1])

            check = len(lock_0)
            for key_loc in key_1_trans:
                try:
                    if lock[key_loc[0]][key_loc[1]] == 0:
                        print(key_loc)
                        check -= 1
                    else:
                        break
                except:
                    pass

            if check == 0:
                return True

    return False


def rotate90(loc):
    res = []
    for i in loc:
        res.append((-1 * i[1], i[0]))

    return res


def trans(loc, x, y):
    res = []
    for i in loc:
        res.append((i[0] + x, i[1] + y))

    return res


a = [[1,1],[1,1]]
b = [[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

print(solution(a, b))
