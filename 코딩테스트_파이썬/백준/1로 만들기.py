def sol():
    first = int(input())
    last = [first]
    cnt = 0

    while True:
        tmp = set()
        for i in last:
            if i == 1:
                print(cnt)
                return

            if i % 2 == 0:
                tmp.add(i // 2)

            if i % 3 == 0:
                tmp.add(i // 3)

            tmp.add(i - 1)
        last = tmp
        cnt += 1


sol()
