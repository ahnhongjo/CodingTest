def sol():
    n, k = map(int, input().split())
    coins = []
    answer = [0] * (k + 1)

    for _ in range(n):
        coins.append(int(input()))
        if coins[-1]<=k:
            answer[coins[-1]]=1

    coins.sort()

    for coin in coins:
        for i in range(coin, k + 1):
            if answer[i - coin] == 0:
                continue
            if answer[i] == 0:
                answer[i] = answer[i - coin] + 1
            else:
                answer[i] = min(answer[i], answer[i - coin] + 1)

    if answer[-1] == 0:
        print(-1)
    else:
        print(answer[-1])



sol()
