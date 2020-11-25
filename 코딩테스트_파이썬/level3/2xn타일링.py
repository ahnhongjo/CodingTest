def solution(n):
    answer = [0 for i in range(n)]

    answer[0] = 1
    answer[1] = 2

    for i in range(2, n):
        answer[i] = answer[i - 1] + answer[i - 2]
        if answer[i] > 1000000007:
            answer[i] = answer[i] % 1000000007

    return answer[n - 1]