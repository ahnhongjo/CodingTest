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
    if len(lock_0) == 0:
        return True
    for i in range(4):
        key_1 = rotate90(key_1)

        for key_one in key_1:
            key_1_trans = trans(key_1, lock_0[0][0] - key_one[0], lock_0[0][1] - key_one[1])

            check = len(lock_0)
            for key_loc in key_1_trans:
                if key_loc[0] < 0 or key_loc[0] >= len(lock) or key_loc[1] < 0 or key_loc[1] >= len(lock):
                    continue
                else:
                    if lock[key_loc[0]][key_loc[1]]==0:
                        check-=1
                    else:
                        check+=1

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
