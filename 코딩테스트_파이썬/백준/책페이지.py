def sol():
    num = int(input())
    nums = [0] * 10

    str_num = str(num)
    for i in range(len(str_num)):
        if i == 0:
            for j in range(1, int(str_num[0]) + 1):
                if j == int(str_num[0]):
                    if len(str_num) == 1:
                        nums[j] += 1
                    else:
                        nums[j] += (int(str_num[1:]) + 1)
                else:
                    nums[j] += 10 ** (len(str_num) - 1)

        elif i == len(str_num) - 1:
            for j in range(10):
                if j <= int(str_num[-1]) and j != 0:
                    nums[j] += (int(str_num[:-1]) + 1)
                else:
                    nums[j] += int(str_num[:-1])

        else:
            for j in range(10):
                if j == int(str_num[i]):
                    if j == 0:
                        tmp = int(str_num[i + 1:]) + 1
                        tmp += (int(str_num[:i]) - 1) * (10 ** len(str_num[i + 1:]))
                    else:
                        tmp = int(str_num[i + 1:]) + 1
                        tmp += (int(str_num[:i])) * (10 ** len(str_num[i + 1:]))

                elif j > int(str_num[i]):
                    tmp = 0
                    tmp += (int(str_num[:i])) * (10 ** len(str_num[i + 1:]))
                else:
                    tmp = 0
                    if j == 0:
                        tmp += (int(str_num[:i])) * (10 ** len(str_num[i + 1:]))
                    else:
                        tmp += (int(str_num[:i]) + 1) * (10 ** len(str_num[i + 1:]))

                nums[j] += tmp

    for i in nums:
        print(i, end=" ")


sol()
