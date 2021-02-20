def sol():
    num=int(input())
    max=0
    ask=[]
    for i in range(num):
        tmp=list(map(str, input().split(" ")))
        if int(tmp[0])>max:
            max=int(tmp[0])
        ask.append(tmp[1])

    S=input().split()
    S=S[1]

    for i in range(max,len(S)+1):
        for j in range(len(S)-i):
            tmp_str=S[j:j+i]
            check=0
            for cmp_str in ask:
                if cmp_str in tmp_str:
                    check+=1
                else:
                    break
            if check==num:
                print(len(tmp_str))
                return

    print(len(S))

sol()