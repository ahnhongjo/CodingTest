def solution(numbers):
    str_num = list(map(str, numbers))
    sort_num = sorted(str_num, key=lambda x: find_key(x))

    answer = ''
    for i in sort_num:
        answer += i

    while answer[0] == "0" and len(answer) > 1:
        answer = answer[1:len(answer)]

    return answer


def find_key(x):
    if len(x) == 1:
        return -int(x), -int(x), -int(x), -int(x), -int(x), -int(x)
    elif len(x) == 2:
        return -int(x[0]), -int(x[1]), -int(x[0]), -int(x[1]), -int(x[0]), -int(x[1])
    elif len(x) == 3:
        return -int(x[0]), -int(x[1]), -int(x[2]), -int(x[0]), -int(x[1]), -int(x[2])
    else:
        return -1, 0, 0, 0