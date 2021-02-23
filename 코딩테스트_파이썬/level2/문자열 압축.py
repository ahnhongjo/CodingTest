def solution(s):
    length = len(s)
    if length == 1:
        return 1

    shortLen = 1000

    for i in range(1, length):
        tmp = []
        for x in range(0, length, i):
            tmp.append(s[x:x + i])

        complen = compress(tmp)

        if shortLen > complen:
            shortLen = complen

    answer = shortLen
    return answer


def compress(sList):
    nowStr = sList[0]
    cmpStr = ""
    cnt = 1
    for i in range(1, len(sList)):
        if nowStr != sList[i]:
            if (cnt == 1):
                cmpStr = cmpStr + nowStr
            else:
                cmpStr = cmpStr + str(cnt) + nowStr
            nowStr = sList[i]
            cnt = 1
            continue
        else:
            cnt = cnt + 1

    if (cnt == 1):
        cmpStr = cmpStr + nowStr
    else:
        cmpStr = cmpStr + str(cnt) + nowStr

    return len(cmpStr)