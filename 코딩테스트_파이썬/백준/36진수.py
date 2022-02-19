def sol():
    num_to_36 = {}
    alpha_to_num = {}
    numbers = [[] for i in range(100)]
    effect = {}

    for i in range(10):
        num_to_36[i] = str(i)
        alpha_to_num[str(i)] = i

    for j in range(26):
        num_to_36[j + 10] = chr(65 + j)
        alpha_to_num[chr(65 + j)] = 10 + j
    num = int(input())

    for _ in range(num):
        tmp = input()
        for i in range(len(tmp)):
            numbers[len(tmp) - i - 1].append(alpha_to_num[tmp[i]])
            if tmp[i] in effect:
                effect[tmp[i]] += 36 ** (len(tmp) - i - 1)
            else:
                effect[tmp[i]] = 36 ** (len(tmp) - i - 1)
    k = int(input())
    effect = sorted(effect.items(), key=lambda item: item[1]*(35-alpha_to_num[item[0]]), reverse=True)
    effect_set = set()

    for i in range(min(k,len(effect))):
        effect_set.add(effect[i][0])

    flag = 0
    answer = ""

    for i in numbers:
        if i == [] and flag == 0:
            break
        tmp = flag
        for j in i:
            if num_to_36[j] in effect_set:
                tmp += 35
            else:
                tmp += j

        flag = tmp // 36
        answer = num_to_36[tmp % 36] + answer

    if num==0 and k==0:
        print(0)
    else:
        print(answer)

sol()
