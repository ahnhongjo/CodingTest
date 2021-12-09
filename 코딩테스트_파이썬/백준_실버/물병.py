def sol():
    n, k =map(int,input().split(" "))

    two_power_n=[1]
    tmp = [1]

    while len(two_power_n) < 2*n:
        tmp=plusplus1(tmp)
        two_power_n += tmp

    pos = n -1
    while True:
        if two_power_n[pos]<=k:
            print(pos-n+1)
            return pos
        pos+=1


def plusplus1(numlist):
    res =[]
    for i in numlist:
        res.append(i)
    for i in numlist:
        res.append(i+1)

    return res

sol()