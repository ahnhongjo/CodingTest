
def sol():
    num = int(input())
    buy = []
    for _ in range(num):
        buy.append(list(map(int, input())))
    dp = [[[0] * 10 for i in range(1 << 15)] for j in range(15)]
    answer = memoization(0, 1, 0, dp, buy, num)

    print(answer+1)


def memoization(pos, visited, price, dp, buy, num):
    if dp[pos][visited][price] != 0:
        return dp[pos][visited][price]

    visit_num = 0

    for i in range(num):
        if buy[pos][i] >= price:
            if not visited & (1 << i):
                visit_num = max(visit_num, 1 + memoization(i, visited | (1 << i), buy[pos][i], dp, buy, num))

    dp[pos][visited][price] = visit_num

    return visit_num


sol()
