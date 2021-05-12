def solution(s):
    eng_to_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                  "nine": 9}

    sub = ""
    answer = ""
    for i in s:
        if i.isdigit():
            answer += i
            continue

        sub += i
        if sub in eng_to_num:
            answer += str(eng_to_num[sub])
            sub = ""

    return int(answer)


print(solution("nineninenine"))
