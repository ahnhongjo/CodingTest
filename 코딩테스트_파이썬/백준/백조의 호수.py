def sol():
    row, col = map(int, input().split())
    ice = []
    goose = []

    for i in range(row):
        tmp = input()
        tmplist = []
        for j in tmp:
            if j == "L":
                goose.append((len(ice), len(tmplist)))
            tmplist.append(j)
        ice.append(tmplist)

    ice, meet = color(ice, goose[0], goose[1])

    if meet:
        print(0)
        return

    day = 1
    while True:
        ice,meet = meltice(ice, row, col)
        if meet:
            print(day)
            return
        for i in ice:
            print(i)
        if day==2:
            return
        day += 1


def meltice(ice, row, col):
    meet=False
    for i in range(row):
        for j in range(col):
            if ice[i][j]=="X":
                continue

            if i + 1 < row and (ice[i][j]=="." or ice[i][j]=="g1" or ice[i][j]=="g2") and ice[i + 1][j] == "X":
                ice[i + 1][j] = "-"+ice[i][j]
            if j + 1 < col and (ice[i][j]=="." or ice[i][j]=="g1" or ice[i][j]=="g2") and ice[i][j + 1] == "X":
                ice[i][j + 1] = "-"+ice[i][j]
            if i - 1 >= 0 and (ice[i][j]=="." or ice[i][j]=="g1" or ice[i][j]=="g2") and ice[i - 1][j] == "X":
                ice[i - 1][j] = "-"+ice[i][j]
            if j - 1 >= 0 and (ice[i][j]=="." or ice[i][j]=="g1" or ice[i][j]=="g2") and ice[i][j - 1] == "X":
                ice[i][j - 1] = "-"+ice[i][j]

    for i in range(row):
        for j in range(col):
            if ice[i][j][0] == "-":
                ice[i][j] = ice[i][j][1:]
    return ice,meet


def color(ice, g1, g2):
    row = len(ice)
    col = len(ice[0])

    q = [g1]
    while q:
        tmp = q[0]
        del q[0]
        ice[tmp[0]][tmp[1]] = "g1"

        if tmp[0] + 1 < row and ice[tmp[0] + 1][tmp[1]] != "X" and ice[tmp[0] + 1][tmp[1]] != "g1":
            q.append((tmp[0] + 1, tmp[1]))
        if tmp[0] - 1 >= 0 and ice[tmp[0] - 1][tmp[1]] != "X" and ice[tmp[0] - 1][tmp[1]] != "g1":
            q.append((tmp[0] - 1, tmp[1]))
        if tmp[1] + 1 < col and ice[tmp[0]][tmp[1] + 1] != "X" and ice[tmp[0]][tmp[1] + 1] != "g1":
            q.append((tmp[0], tmp[1] + 1))
        if tmp[1] - 1 >= 0 and ice[tmp[0]][tmp[1] - 1] != "X" and ice[tmp[0]][tmp[1] - 1] != "g1":
            q.append((tmp[0], tmp[1] - 1))

    q = [g2]
    while q:
        tmp = q[0]
        del q[0]

        if ice[tmp[0]][tmp[1]] == "g1":
            return ice, True

        ice[tmp[0]][tmp[1]] = "g2"

        if tmp[0] + 1 < row and ice[tmp[0] + 1][tmp[1]] != "X" and ice[tmp[0] + 1][tmp[1]] != "g2":
            q.append((tmp[0] + 1, tmp[1]))
        if tmp[0] - 1 >= 0 and ice[tmp[0] - 1][tmp[1]] != "X" and ice[tmp[0] - 1][tmp[1]] != "g2":
            q.append((tmp[0] - 1, tmp[1]))
        if tmp[1] + 1 < col and ice[tmp[0]][tmp[1] + 1] != "X" and ice[tmp[0]][tmp[1] + 1] != "g2":
            q.append((tmp[0], tmp[1] + 1))
        if tmp[1] - 1 >= 0 and ice[tmp[0]][tmp[1] - 1] != "X" and ice[tmp[0]][tmp[1] - 1] != "g2":
            q.append((tmp[0], tmp[1] - 1))

    return ice, False


sol()
