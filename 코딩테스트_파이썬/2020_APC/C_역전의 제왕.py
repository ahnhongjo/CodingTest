def sol():
    tmp = list(map(int, input().split()))

    people_num = tmp[0]
    input_num = tmp[1]
    people_score = []
    freeze_problem = []

    for i in range(1, people_num + 1):
        people_score.append({"id": i , "problem": 0, "penalty": 0, "last_answer": 0,
                             "order": 0, "after_order": 0, "reverse": 0})

    for i in range(input_num):

        tmp = input().split()

        time = tmp[0]
        person = people_score[int(tmp[1])-1]
        problem_num = tmp[2]
        sub = tmp[3]

        penalty = int(time[0:2]) * 60 + int(time[3:5]) + (int(sub) - 1) * 20

        if time > "03:00":
            freeze_problem.append(tmp)

        else:
            person["problem"] += 1
            person["penalty"] += penalty
            person["last_answer"] = i

    sort_score=sorted(people_score,key=lambda x:(-x["problem"],x["penalty"],x["last_answer"]))
    for i in range(len(sort_score)):
        sort_score[i]["order"]=i+1
        print(sort_score[i])
    last_id=sort_score[2]["id"]
    print(last_id)
    print(freeze_problem)


sol()
