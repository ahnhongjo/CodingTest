import copy
from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    answer_list=[]
    max_score_diff = 1
    for ryan_info in combinations_with_replacement(range(11),n):
        tmp =[0]*11
        for i in ryan_info:
            tmp[i]+=1
        score_dif = score_diff(tmp,info)
        if max_score_diff < score_dif:
            answer_list=[]
            answer_list.append(tmp)
            max_score_diff = score_dif
        elif max_score_diff == score_dif:
            answer_list.append(tmp)

    answer_list.sort(key=lambda x :sort_key(x),reverse=True)

    if not answer_list:
        return [-1]
    return answer_list[0]

def score_diff(ryan,apeach):
    ryan_score=0
    apeach_score=0
    for i in range(11):
        if ryan[i] == 0 and apeach[i] ==0:
            continue
        elif ryan[i] >apeach[i]:
            ryan_score+=(10-i)
        else:
            apeach_score+=(10-i)

    return ryan_score-apeach_score

def sort_key(x):
    ret=""
    for i in x:
        ret = str(i)+ret

    return int(ret)



solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])