def sol():
    marking = [True for i in range(10000)]

    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    check_num = 1001 * a + 101 * b + 11 * c + 2 * d
                    if 10000 >= check_num >= 1:
                        marking[check_num - 1] = False

    for i in range(1, 10001):
        if marking[i-1]:
            print(i)

sol()
