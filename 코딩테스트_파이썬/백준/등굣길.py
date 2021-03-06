def solution(m, n, puddles):
    maps=[[-1 for i in range(m)]for j in range(n)]

    for puddle in puddles:
        maps[puddle[1]-1][puddle[0]-1]=0

    num = 1
    for i in range(n):
        if maps[i][0]==0:
            num=0
        maps[i][0]=num

    num = 1
    for i in range(m):
        if maps[0][i]==0:
            num=0
        maps[0][i]=num

    for i in range(1,n):
        for j in range(1,m):
            if maps[i][j]==0:
                continue
            maps[i][j]=(maps[i-1][j]+maps[i][j-1])% 1000000007

    for map in maps:
        print(map)
    return maps[n-1][m-1]

print(solution(1,3,[[1,2]]))