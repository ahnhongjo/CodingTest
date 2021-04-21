def solution(s):
    set_list = []
    num = ""
    tmp = []
    for i in s:
        if i == "{":
            tmp = []

        elif i == "}":
            if len(num) != 0:
                tmp.append(int(num))
                set_list.append(tmp)
                num = ""
                tmp = []

        elif i == ",":
            if len(num) != 0:
                tmp.append(int(num))
                num = ""

        else:
            num += i

    set_list_sort = sorted(set_list, key=lambda x: len(x))
    answer = []

    for i in set_list_sort:
        for j in i:
            if not j in answer:
                answer.append(j)
                break

    print(answer)
    return answer


solution("{{123}}")
