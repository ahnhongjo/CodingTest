def solution(enroll, referral, seller, amount):
    tree = [["-", "-", 0]]
    name_num = {"-": 0}

    num = 0
    for i in enroll:
        tree.append([i, referral[num], 0])
        name_num[i] = num + 1
        num += 1


    for i in range(len(seller)):
        sel_num = name_num[seller[i]]

        up_money=amount[i]*100
        while True:
            tree[sel_num][2] += up_money-(up_money//10)
            up_money=up_money//10
            if tree[sel_num][0]=="-":
                break
            sel_num=name_num[tree[sel_num][1]]

    answer = []
    for i in tree:
        answer.append(i[2])

    del answer[0]
    print(answer)
    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
         ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10])

# print([360, 958, 108, 0, 450, 18, 180, 1080])
