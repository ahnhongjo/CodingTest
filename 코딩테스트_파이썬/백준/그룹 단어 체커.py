def sol():
    num = int(input())
    answer=0

    for i in range(num):
        tmp_str=input()
        answer+=check(tmp_str)

    print(answer)


def check(tmp_str):
    for ch in range(len(tmp_str)):
        if ch==len(tmp_str)-1 or tmp_str[ch] == tmp_str[ch + 1]:
            continue
        else:
            if tmp_str[ch] in tmp_str[ch + 1:]:
                return 0
    return 1

sol()