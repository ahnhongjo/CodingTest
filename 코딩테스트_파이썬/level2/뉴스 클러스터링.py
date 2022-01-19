def solution(str1, str2):
    answer = 0
    str1_dup = []
    str2_dup = []

    for i in range(len(str1) - 1):
        tmpstr = str1[i] + str1[i + 1]
        tmplowstr = str_low(tmpstr)
        if tmplowstr:
            str1_dup.append(tmplowstr)
    for i in range(len(str2) - 1):
        tmpstr = str2[i] + str2[i + 1]
        tmplowstr = str_low(tmpstr)
        if tmplowstr:
            str2_dup.append(tmplowstr)

    if len(str1_dup) == 0 and len(str2_dup) == 0:
        return 65536

    shr_n = share_num(str1_dup,str2_dup)
    answer = 65536 * shr_n//(len(str1_dup)+len(str2_dup))

    print(answer)

    return answer


def str_low(tmpstr):
    if tmpstr.isalpha():
        tmpstr = tmpstr.lower()
        return tmpstr
    else:
        return False


def share_num(list1,list2):
    num =0
    for i in list1:
        if i in list2:
            list2.remove(i)
            num+=1
    return num



solution("aa1+aa2", "AAAA12")
