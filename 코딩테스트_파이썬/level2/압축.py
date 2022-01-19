def solution(msg):
    press_dic = {}

    for i in range(26):
        press_dic[chr(ord('A')+i)] =i+1

    answer = []

    start = msg[0]
    pos = 1

    while True:
        while pos <len(msg) and (start + msg[pos]) in press_dic:
            start = start + msg[pos]
            pos +=1

        if pos >=len(msg):
            answer.append(press_dic[start])
            break
        tmp = start + msg[pos]
        answer.append(press_dic[start])
        press_dic[tmp] = len(press_dic)+1
        start = msg[pos]
        pos +=1

    return answer

print(solution('KAKAO'))