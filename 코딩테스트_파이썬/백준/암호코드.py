def sol():
    num = list(input())
    answer = [[0] * len(num) for i in range(2)]

    for i in range(len(num)):
        if i == 0:
            if num[i] == '0':
                print(0)
                return
            answer[0][0] = 1
            answer[1][0] = 0
        else:
            if num[i] == '0':
                if num[i - 1] != '1' and num[i - 1] != '2':
                    print(0)
                    return
                answer[0][i] = 0
            else:
                answer[0][i] = (answer[0][i - 1] + answer[1][i - 1]) % 1000000

            if 10 <= int(num[i - 1] + num[i]) <= 26:
                answer[1][i] = answer[0][i - 1]
            else:
                answer[1][i] = 0

    print((answer[0][-1] + answer[1][-1])%1000000)

sol()
