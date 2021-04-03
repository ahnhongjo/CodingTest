def solution(lottos, win_nums):
    num_0 = 0
    right_num = 0

    for i in lottos:
        if i in win_nums:
            right_num += 1
        elif i == 0:
            num_0 += 1

    answer = []

    best = 7 - right_num - num_0
    worst = 7 - right_num
    if best >= 6:
        best = 6

    if worst >= 6:
        worst = 6
    answer.append(best)
    answer.append(worst)

    print(answer)

    return answer

solution([1,2,3,4,5,6],	[38, 19, 20, 40, 15, 25])