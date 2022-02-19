from itertools import permutations

def solution(board, r, c):
    answer = 0
    picture={}
    for i in range(4):
        for j in range(4):
            tmp = board[i][j]
            if tmp==0:
                continue
            if tmp in picture:
                picture[tmp].append((i,j))
            else:
                picture[tmp]=[(i,j)]
    tmp = [i+1 for i in range(len(picture))]
    order = list(permutations(tmp,len(picture)))

    

    return answer


solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
