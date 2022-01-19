from itertools import product

def solution(info, query):
    answer = []
    order=dict()
    language = ["cpp","java","python","-"]
    frontback =["frontend","backend","-"]
    year=["junior","senior","-"]
    soulfood=["chicken","pizza","-"]

    for i in info:
        p_info = list(i.split(" "))
        keys =list(product([p_info[0],"-"],[p_info[1],"-"],[p_info[2],"-"],[p_info[3],"-"],repeat=1))
        for key in keys:
            if key in order:
                order[key].append(int(p_info[4]))
            else:
                order[key]=[int(p_info[4])]

    for i in order.values():
        i.sort()

    for q in query:
        q_list = list(q.split(" "))
        key = (q_list[0],q_list[2],q_list[4],q_list[6])

        if key not in order:
            answer.append(0)
            continue

        volunteers = order[key]
        start =0
        end =len(volunteers)-1
        findnum = int(q_list[-1])

        while start <= end:
            mid =(start+end)//2

            if volunteers[mid] <findnum:
                start = mid+1
            else:
                end = mid-1

        answer.append(len(volunteers)-mid)

    print(answer)
    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
