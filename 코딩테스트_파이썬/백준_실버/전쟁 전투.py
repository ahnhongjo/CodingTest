from collections import deque

def sol():
    #n 가로, m 세로
    n,m = map(int,input().split())
    power={'W':0,'B':0}
    formation=[]
    for _ in range(m):
        tmp = list(input())
        formation.append(tmp)

    for i in range(m):
        for j in range(n):
            if formation[i][j] =='.':
                continue
            else:
                flag = formation[i][j]
                power[flag] += power_part([i,j],formation,n,m)

    print(power['W'],end=" ")
    print(power['B'], end=" ")

def power_part(pos,formation,n,m):
    q = deque([])
    q.append(pos)
    flag = formation[pos[0]][pos[1]]
    army = 0

    while q:
        nowpos = q.popleft()
        x = nowpos[0]
        y = nowpos[1]
        if formation[x][y] ==flag:
            formation[x][y] = '.'
            army += 1

        if x-1>=0 and formation[x-1][y] ==flag:
            q.append([x-1,y])
        if x+1< m and formation[x+1][y] ==flag:
            q.append([x+1,y])
        if y-1>=0 and formation[x][y-1] ==flag:
            q.append([x,y-1])
        if y+1< n and formation[x][y+1] ==flag:
            q.append([x,y+1])
    return army*army

sol()