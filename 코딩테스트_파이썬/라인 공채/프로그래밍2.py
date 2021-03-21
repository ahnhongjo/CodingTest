def solution(inp_str):
    answer = []
    tmp_answer = []

    # 1
    if len(inp_str) < 8 or len(inp_str) > 15:
        tmp_answer.append(1)

    #2
    if inp_str!="^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$":
        pass
    return answer
# solution()

