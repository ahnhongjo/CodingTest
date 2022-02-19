from itertools import permutations
import copy


def solution(n, weak, dist):
    for i in range(1, len(dist) + 1):
        orders = permutations(dist, i)
        for order in orders:
            if i == 1:
                if cover_pos(weak, list(order), n):
                    return i
            if cover_pos(weak, order, n):
                return i

    return -1


def cover_pos(weak, order, n):
    tmp = copy.deepcopy(weak)

    for i in weak:
        tmp.append(i + n)

    for i in range(len(tmp) // 2):
        order_num = 0
        cover_cnt = 0
        start = weak[i]
        end = start + order[order_num]
        order_num+=1
        for j in tmp[i:]:
            if cover_cnt == len(weak):
                return True
            if j <= end:
                cover_cnt += 1
                continue
            else:
                if order_num >= len(order):
                    break
                start = j
                end = start + order[order_num]
                cover_cnt += 1
                order_num += 1

    return False


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
