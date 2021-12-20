from collections import deque

def sol():
    r, c = map(int,input().split())
    mineral = []

    for _ in range(r):
        mineral.append(list(input()))

    left_right = 1

    n = int(input())
    height = list(map(int,input().split()))
    for i in height:
        mineral_pos =(-1,-1)
        if left_right ==1:
            for j in range(c):
                if mineral[r - i][j] == 'x':
                    mineral[r - i][j] = '.'
                    mineral_pos = (r - i, j)
                    break
        else:
            for j in range(c-1,-1,-1):
                if mineral[r - i][j] == 'x':
                    mineral[r - i][j] = '.'
                    mineral_pos = (r - i, j)
                    break
        if mineral_pos[0]>-1:
            downing(mineral_pos,mineral,left_right,r,c)
        left_right *= -1

    for i in mineral:
        print("".join(i))

def downing(mineral_pos,mineral,left_right,r,c):
    #위
    cluster=[]
    q = deque()
    checkup = (mineral_pos[0]-1,mineral_pos[1])
    if checkup[0]>=0 and mineral[checkup[0]][checkup[1]] =='x':
        mineral[checkup[0]][checkup[1]] = '.'
        cluster.append([checkup[0],checkup[1]])

        q.append(cluster[0])

    while q:
        nownode = q.popleft()
        if nownode[0] - 1 >= 0 and mineral[nownode[0]-1][nownode[1]] =='x':
            mineral[nownode[0] - 1][nownode[1]] = '.'
            cluster.append([nownode[0]-1,nownode[1]])
            q.append([nownode[0]-1,nownode[1]])

        if nownode[0] + 1 == r-1 and mineral[nownode[0] + 1][nownode[1]] == 'x':
            break

        if nownode[0] + 1 < r and mineral[nownode[0]+1][nownode[1]] =='x':
            mineral[nownode[0] + 1][nownode[1]] = '.'
            cluster.append([nownode[0]+1,nownode[1]])
            q.append([nownode[0]+1,nownode[1]])
        if nownode[1] - 1 >= 0 and mineral[nownode[0]][nownode[1]-1] =='x':
            mineral[nownode[0]][nownode[1]-1] = '.'
            cluster.append([nownode[0],nownode[1]-1])
            q.append([nownode[0],nownode[1]-1])
        if nownode[1] + 1 <c and mineral[nownode[0]][nownode[1]+1] =='x':
            mineral[nownode[0]][nownode[1]+1] = '.'
            cluster.append([nownode[0],nownode[1]+1])
            q.append([nownode[0],nownode[1]+1])

    down = 0
    continue_pos = True
    while continue_pos and len(cluster) != 0:
        down +=1
        for i in cluster:
            if i[0]+down < r and mineral[i[0]+down][i[1]] !='x':
                continue
            else:
                down -= 1
                continue_pos = False
                break

    for i in cluster:
        mineral[i[0] + down][i[1]] = 'x'

    if down != 0:
        return

    #옆
    cluster = []
    q=deque()
    check_beside = (mineral_pos[0], mineral_pos[1]+left_right)
    if left_right == 1 and check_beside[1] < c and mineral[check_beside[0]][check_beside[1]] =='x':
        mineral[check_beside[0]][check_beside[1]] ='.'
        cluster.append([check_beside[0],check_beside[1]])
        q.append(cluster[0])
    elif left_right == -1 and check_beside[1] >=0 and mineral[check_beside[0]][check_beside[1]] =='x':
        mineral[check_beside[0]][check_beside[1]] = '.'
        cluster.append([check_beside[0], check_beside[1]])
        q.append(cluster[0])

    while q:
        nownode = q.popleft()
        if nownode[0] - 1 >= 0 and mineral[nownode[0] - 1][nownode[1]] == 'x':
            mineral[nownode[0] - 1][nownode[1]] = '.'
            cluster.append([nownode[0] - 1, nownode[1]])
            q.append([nownode[0] - 1, nownode[1]])

        if nownode[0] + 1 == r - 1 and mineral[nownode[0] + 1][nownode[1]] == 'x':
            break

        if nownode[0] + 1 < r and mineral[nownode[0] + 1][nownode[1]] == 'x':
            mineral[nownode[0] + 1][nownode[1]] = '.'
            cluster.append([nownode[0] + 1, nownode[1]])
            q.append([nownode[0] + 1, nownode[1]])
        if nownode[1] - 1 >= 0 and mineral[nownode[0]][nownode[1] - 1] == 'x':
            mineral[nownode[0]][nownode[1] - 1] = '.'
            cluster.append([nownode[0], nownode[1] - 1])
            q.append([nownode[0], nownode[1] - 1])
        if nownode[1] + 1 < c and mineral[nownode[0]][nownode[1] + 1] == 'x':
            mineral[nownode[0]][nownode[1] + 1] = '.'
            cluster.append([nownode[0], nownode[1] + 1])
            q.append([nownode[0], nownode[1] + 1])

    down = 0
    continue_pos = True
    while continue_pos and len(cluster) != 0:
        down += 1
        for i in cluster:
            if i[0] + down < r and mineral[i[0] + down][i[1]] != 'x':
                continue
            else:
                down -= 1
                continue_pos = False
                break

    for i in cluster:
        mineral[i[0] + down][i[1]] = 'x'

    if down != 0:
        return


    #아래
    cluster = []
    q=deque()
    check_down = (mineral_pos[0] + 1, mineral_pos[1])
    if check_down[0] < r and mineral[check_down[0]][check_down[1]] == 'x':
        mineral[check_down[0]][check_down[1]] = '.'
        cluster.append([check_down[0], check_down[1]])

        q.append(cluster[0])

    while q:
        nownode = q.popleft()
        if nownode[0] - 1 >= 0 and mineral[nownode[0] - 1][nownode[1]] == 'x':
            mineral[nownode[0] - 1][nownode[1]] = '.'
            cluster.append([nownode[0] - 1, nownode[1]])
            q.append([nownode[0] - 1, nownode[1]])

        if nownode[0] + 1 == r - 1 and mineral[nownode[0] + 1][nownode[1]] == 'x':
            break

        if nownode[0] + 1 < r and mineral[nownode[0] + 1][nownode[1]] == 'x':
            mineral[nownode[0] + 1][nownode[1]] = '.'
            cluster.append([nownode[0] + 1, nownode[1]])
            q.append([nownode[0] + 1, nownode[1]])
        if nownode[1] - 1 >= 0 and mineral[nownode[0]][nownode[1] - 1] == 'x':
            mineral[nownode[0]][nownode[1] - 1] = '.'
            cluster.append([nownode[0], nownode[1] - 1])
            q.append([nownode[0], nownode[1] - 1])
        if nownode[1] + 1 < c and mineral[nownode[0]][nownode[1] + 1] == 'x':
            mineral[nownode[0]][nownode[1] + 1] = '.'
            cluster.append([nownode[0], nownode[1] + 1])
            q.append([nownode[0], nownode[1] + 1])

    down = 0
    continue_pos = True
    while continue_pos and len(cluster) != 0:
        down += 1
        for i in cluster:
            if i[0] + down < r and mineral[i[0] + down][i[1]] != 'x':
                continue
            else:
                down -= 1
                continue_pos = False
                break

    for i in cluster:
        mineral[i[0] + down][i[1]] = 'x'

    if down != 0:
        return

sol()
