def solution(id_list, report, k):
    answer = []
    user_report={}
    user_num={}

    report = set(report)
    for i in id_list:
        user_num[i]=0
        user_report[i]=[]

    for i in report:
        split_report=i.split()
        user_report[split_report[0]].append(split_report[1])
        user_num[split_report[1]] += 1

    for i in id_list:
        mail_num=0

        report_list=user_report[i]
        for j in report_list:
            if user_num[j]>=k:
                mail_num+=1
        answer.append(mail_num)

    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)