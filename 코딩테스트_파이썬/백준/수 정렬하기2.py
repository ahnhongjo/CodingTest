def sol():
    iter_num = int(input())

    answer = [False] * 2000001

    for i in range(iter_num):
        answer[int(input()) + 1000000] = True

    for i in range(len(answer)):
        if answer[i]:
            print(i - 1000000)


sol()