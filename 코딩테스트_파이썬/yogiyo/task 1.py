# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    list_s = S.split("; ")
    list_email = []

    for i in list_s:
        tmp_name = i.split(" ")
        tmp_last = tmp_name[-1].lower()
        tmp_last = tmp_last.replace("-", "")
        tmp_first = tmp_name[0].lower()
        tmp_first = tmp_first.replace("-", "")
        tmp_email = tmp_last + "_" + tmp_first + "@" + C.lower() + ".com"
        num = 2
        while tmp_email in list_email:
            tmp_email = tmp_last + "_" + tmp_first + str(num) + "@" + C.lower() + ".com"
            num += 1

        list_email.append(tmp_email)

    answer_list=[]

    for i in range(len(list_s)):
        tmp_str=list_s[i]+" "+"<"+list_email[i]+">"
        answer_list.append(tmp_str)

    answer="; ".join(answer_list)

    return answer


s = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; " \
    "John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
c = "example"

solution(s, c)
