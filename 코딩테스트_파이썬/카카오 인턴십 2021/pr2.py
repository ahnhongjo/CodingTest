def solution(places):
    answer = []
    for i in places:
        for j in i:
            print(j)
        print()

    for i in places:
        tmp_place=[]
        for j in i:
            tmp=[]
            for a in j:
                tmp.append(a)
            tmp_place.append(tmp)

        answer.append(check(tmp_place))
    return answer

def check(places):
    for i in range(5):
        for j in range(5):
            if places[i][j]=="P" and not bfs(i,j,places):
                return 0

    return 1


def bfs(i, j, places):
    q = [(i, j)]

    for i in range(2):
        while q:
            tmp_q=[]
            tmp = q.pop()
            places[tmp[0]][tmp[1]]="X"

            if tmp[0] + 1 < 5 and places[tmp[0] + 1][tmp[1]] != "X":
                if places[tmp[0] + 1][tmp[1]] == "P":
                    return False
                tmp_q.append((tmp[0] + 1, tmp[1]))

            if tmp[1] + 1 < 5 and places[tmp[0]][tmp[1] + 1] != "X":
                if places[tmp[0]][tmp[1] + 1] == "P":
                    return False
                tmp_q.append((tmp[0], tmp[1] + 1))

            if tmp[0] - 1 >= 0 and places[tmp[0] - 1][tmp[1]] != "X":
                if places[tmp[0] - 1][tmp[1]] == "P":
                    return False
                tmp_q.append((tmp[0] - 1, tmp[1]))

            if tmp[1] - 1 >= 0 and places[tmp[0]][tmp[1] - 1] != "X":
                if places[tmp[0]][tmp[1] - 1] == "P":
                    return False
                tmp_q.append((tmp[0], tmp[1] - 1))
        q=tmp_q

    return True


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
