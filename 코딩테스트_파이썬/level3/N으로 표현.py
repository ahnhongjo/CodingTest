def solution(N, number):
    if N == number:
        return 1
    make_num = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(1, i):
            for x in make_num[j - 1]:
                for y in make_num[i - j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            return i
        make_num.append(numbers)

    return -1
