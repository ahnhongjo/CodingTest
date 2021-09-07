def solution(s):
    answer_list=s.split(" ")
    answer = ''
    print(answer_list)
    for i in answer_list:
        if i=="":
            answer+=" "
            continue
        if i[0].isdigit():
            answer+=i.lower()
            answer+=" "
        else:
            answer=answer+i[0].upper()+i[1:].lower()
            answer+=" "

    answer=answer[:-1]
    print(answer)
    return answer


solution("3people ")

