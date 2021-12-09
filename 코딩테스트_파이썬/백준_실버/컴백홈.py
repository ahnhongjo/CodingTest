import copy
global answer
def sol():
    r, c, k = map(int, input().split())

    thismap = []
    for i in range(r):
        tmp = list(input())
        thismap.append(tmp)


    thismap[r - 1][0] = 'T'
    findroad((r - 1, 0), thismap, k - 1,r,c)

def findroad(pos, thismap, remain,r,c):
    if remain == 0:
        if pos[0] ==0 and pos[1]==c-1:
            global answer
            answer+=1
            return
        else:
            return

    if pos[0] -1>=0 and thismap[pos[0] - 1][pos[1]] != 'T':
        tmpmap=copy.deepcopy(thismap)
        tmpmap[pos[0]-1][pos[1]] ='T'
        findroad((pos[0]-1,pos[1]),tmpmap,remain-1,r,c)


    if pos[0]+1 <r and thismap[pos[0] + 1][pos[1]] != 'T':
        tmpmap = copy.deepcopy(thismap)
        tmpmap[pos[0] + 1][pos[1]] = 'T'
        findroad((pos[0] + 1, pos[1]), tmpmap, remain - 1,r,c)


    if pos[1] - 1>=0 and thismap[pos[0]][pos[1] - 1] != 'T':
        tmpmap = copy.deepcopy(thismap)
        tmpmap[pos[0]][pos[1]-1] = 'T'
        findroad((pos[0], pos[1]-1), tmpmap, remain - 1,r,c)


    if pos[1] + 1<c and thismap[pos[0]][pos[1] + 1] != 'T':
        tmpmap = copy.deepcopy(thismap)
        tmpmap[pos[0]][pos[1]+1] = 'T'
        findroad((pos[0], pos[1]+1), tmpmap, remain - 1,r,c)

answer=0
sol()
print(answer)