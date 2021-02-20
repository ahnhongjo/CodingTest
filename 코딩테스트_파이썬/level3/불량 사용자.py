from itertools import permutations

def solution(user_id, banned_id):
    user_num=len(user_id)
    ban_num=len(banned_id)
    permute=list(permutations(range(user_num),ban_num))
    ban_list=set()

    for i in permute:
        right=0
        for j in range(ban_num):
            if match(user_id[i[j]], banned_id[j]):
                right+=1

        if right==ban_num:
            sorted_tuple=sorted(i)

            ban_list.add(tuple(sorted_tuple))
    return len(ban_list)

def match(normal, ban):
    if len(normal)!=len(ban):
        return False

    for i in range(len(ban)):
        if ban[i]=="*":
            continue

        if ban[i]!=normal[i]:
            return False

    return True

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))