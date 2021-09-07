def solution(n, t, m, p):
    ans_str=""
    num=0
    while len(ans_str)<m*t:
        ans_str+=change(n,num)
        num+=1

    answer = ''
    for i in range(t):
        answer=answer+ans_str[m*i+p-1]

    print(answer)
    return answer


def change(n,num):
    answer=""
    if num==0:
        return str(0)
    while num>0:
        add_num=num%n
        num//=n
        if add_num>=10:
            answer=chr(add_num+55)+answer
        else:
            answer=str(add_num)+answer
    return answer



solution(16, 16, 2, 2)
