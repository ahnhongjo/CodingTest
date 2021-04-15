def solution(s):
    check_num=0
    for i in range(len(s)):
        tmp_s=s[i:]+s[:i]
        check_num=check(tmp_s)
        if check_num!=0:
            break
    answer = check_num
    print(answer)
    return answer


def check(s):
    stack = []
    right_num = 0

    for i in s:

        if i == "(" or i == "[" or i == "{":
            if len(stack) == 0:
                right_num += 1

            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            if i == ")" and stack[-1] == "(":
                del stack[-1]
            elif i == "}" and stack[-1] == "{":
                del stack[-1]
            elif i == "]" and stack[-1] == "[":
                del stack[-1]

    if len(stack)==0:
        return right_num

    else:
        return 0


solution("[)(]")
