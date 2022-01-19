from itertools import combinations


def solution(orders, course):
    answer = []

    for num in course:
        allmenu = set()
        for order in orders:
            allmenu = set.union(allmenu,set(combinations(order,num)))
        tmp_answer = whatmax(allmenu, orders)
        for i in tmp_answer:
            tmp = list(i)
            tmp.sort()
            answer.append("".join(tmp))
    answer =list(set(answer))
    answer.sort()
    return answer


def whatmax(orderlist, orders):
    result = []
    max_cnt = 1
    for one_order in orderlist:
        cnt = 0
        for order in orders:
            cntup = True
            for i in one_order:
                if i not in order:
                    cntup = False
            if cntup:
                cnt += 1
        if cnt ==1:
            continue
        if cnt > max_cnt:
            result = []
            max_cnt = cnt
            result.append(one_order)
            continue
        elif cnt == max_cnt:
            result.append(one_order)

    return result


solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
