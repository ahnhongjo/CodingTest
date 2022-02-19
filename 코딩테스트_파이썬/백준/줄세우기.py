def sol():
    num = int(input())

    dp = [1] * num
    line = []

    for i in range(num):
        tmp = int(input())
        for j in range(len(line)):
            if line[j] < tmp:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        line.append(tmp)

    print(num-max(dp))


sol()
