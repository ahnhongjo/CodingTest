def sol():
    dp = [1, 1, 2]
    num = int(input())
    while len(dp)<=num:
        dp.append(dp[-1]+dp[-2])
    vip_num = int(input())

    start=0
    down_num =1
    for i in range(vip_num):
        end = int(input())
        dp_len = end-start-1
        down_num*=dp[dp_len]
        start = end
    dp_len = num - start
    down_num *= dp[dp_len]
    print(down_num)

sol()
