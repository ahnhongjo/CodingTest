from itertools import combinations

def solution(relation):
    col_num=len(relation[0])
    row_num=len(relation)
    answer = 0
    candidate_key=[]
    key_kind=[]
    for i in range(1,col_num+1):
        tmp=list(combinations(range(col_num),i))
        for key in tmp:
            key_kind.append(key)


    for key in key_kind:
        test_set=set()
        for tup in relation:
            value = ""
            for key_val in key:
                value+=tup[key_val]
            test_set.add(value)
        if len(test_set)==row_num and check_minial(candidate_key,key):
            candidate_key.append(key)

    return len(candidate_key)


def check_minial(candidate,key):
    for candidate_key in candidate:
        differ = 0
        for i in candidate_key:
            if i in key:
                differ+=1
        if differ ==len(candidate_key):
            return False

    return True



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))