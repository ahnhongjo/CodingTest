def sol():
    num = int(input())
    work_time = []
    for _ in range(num):
        t, s = map(int, input().split())
        work_time.append((t, s))
    work_time = sorted(work_time, key=lambda x: (x[1], x[0]))

    start = 0
    while True:
        now = start
        for i in work_time:
            now += i[0]
            if now > i[1]:
                print(start - 1)
                return

        start += 1


sol()