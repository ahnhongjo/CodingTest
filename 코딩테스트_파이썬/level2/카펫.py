def solution(brown, yellow):
    answer = []
    sum = brown + yellow

    for i in range(3, sum // 2):
        if sum % i != 0:
            continue
        if (i - 2) * (sum // i - 2) == yellow:
            answer.append(sum / i)
            answer.append(i)
            return answer

    return 0

