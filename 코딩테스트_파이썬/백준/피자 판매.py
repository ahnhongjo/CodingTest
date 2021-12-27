def sol():
    buy_pizza = int(input())
    m, n = map(int, input().split())
    pizza_a = []
    pizza_a_dict = {}
    pizza_b = []
    pizza_b_dict = {}

    for _ in range(m):
        pizza_a.append(int(input()))

    for _ in range(n):
        pizza_b.append(int(input()))

    len_a = len(pizza_a)
    len_b = len(pizza_b)

    for start in range(len_a):
        tmp_sum = 0

        for i in range(len_a-1):
            tmp_sum+= pizza_a[(start+i)%len_a]

            if tmp_sum in pizza_a_dict:
                pizza_a_dict[tmp_sum] += 1
            else:
                pizza_a_dict[tmp_sum] = 1

    for start in range(len_b):
        tmp_sum = 0

        for i in range(len_b-1):
            tmp_sum+= pizza_b[(start+i)%len_b]

            if tmp_sum in pizza_b_dict:
                pizza_b_dict[tmp_sum] += 1
            else:
                pizza_b_dict[tmp_sum] = 1

    pizza_a_dict[sum(pizza_a)] = 1
    pizza_b_dict[sum(pizza_b)] = 1

    ans = 0
    for i in pizza_a_dict:
        if i > buy_pizza:
            continue

        if i == buy_pizza:
            ans += pizza_a_dict[i]

        elif buy_pizza - i not in pizza_b_dict:
            continue

        else:
            ans += pizza_a_dict[i] * pizza_b_dict[buy_pizza - i]

    if buy_pizza in pizza_b_dict:
        ans += pizza_b_dict[buy_pizza]

    print(ans)

sol()
