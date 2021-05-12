def solution(new_id):
    answer = upper(new_id)
    answer = spe(answer)
    answer = reduce(answer)
    answer = fldot(answer)
    if len(answer)==0:
        answer="a"

    answer=fldot(answer[:15])

    while len(answer)<3:
        answer+=answer[-1]
    print(answer)

    return answer


def upper(id):
    answer = ""
    for i in id:
        if 65 <= ord(i) <= 90:
            answer += chr(ord(i) + 32)
        else:
            answer += i
    return answer


# 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
def spe(id):
    answer = ""
    for i in id:
        if i.isalpha() or i.isdigit() or i == "-" or i == "_" or i == ".":
            answer += i

    return answer


def reduce(id):
    answer = id[0]
    for i in range(1, len(id)):
        if answer[-1] == "." and id[i] == ".":
            continue
        answer += id[i]
    return answer

def fldot(id):
    ans=id
    if id == "." or len(id)==0:
        return ""

    if id[0]==".":
        ans=ans[1:]

    if id[-1]==".":
        ans=ans[:-1]

    return ans


solution("...!@BaT#*..y.abcdefghijklm")
