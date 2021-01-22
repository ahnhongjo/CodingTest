def solution(land):
    num=len(land)

    dp=[[0 for i in range(num)]for j in range(num)]
    pos = [[0 for i in range(num)] for j in range(num)]

    for i in range(num):
        tmp=max(land[i])
        dp[i][i]=tmp
        pos[i][i]=(land[i].index(tmp),land[i].index(tmp))


    for n in range(1,num):
        for i in range(num-n):
            #첫번째 값
            max1=0
            pos1=-1
            for x in range(4):
                if x == pos[i][i+n-1][1]:
                    continue
                if max1<land[i+n][x]:
                    max1=land[i+n][x]
                    pos1=x

            x1=dp[i][i+n-1]+max1

            max2 = 0
            pos2 = -1
            for x in range(4):
                if x == pos[i+1][i+n][0]:
                    continue
                if max2 < land[i][x]:
                    max2 = land[i][x]
                    pos2 = x

            x2=dp[i+1][i+n]+max2

            if x1>x2:
                dp[i][i+n]=x1
                pos[i][i+n]=(pos[i][i+n-1][0],pos1)
            else:
                dp[i][i + n] = x2
                pos[i][i + n] = (pos2,pos[i+1][i+n][1])


    answer = dp[0][num-1]
    return answer

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])