def solution(dirs):
    garo = [[0 for i in range(10)] for j in range(11)]
    sero = [[0 for i in range(11)] for j in range(10)]

    pos = [0, 0]
    newline = 0
    for i in dirs:
        if i == "L" and pos[0] > -5:
            posx = pos[0] + 5
            posy = pos[1] + 4
            pos[0] -= 1

            if garo[posx][posy] == 0:
                newline += 1
                garo[posx][posy] = 1

        elif i == "R" and pos[0] < 5:
            posx = pos[0] + 5
            posy = pos[1] + 5
            pos[0] += 1

            if garo[posx][posy] == 0:
                newline += 1
                garo[posx][posy] = 1

        elif i == "U" and pos[1] < 5:
            posx = pos[0] + 4
            posy = pos[1] + 5
            pos[1] += 1

            if sero[posx][posy] == 0:
                newline += 1
                sero[posx][posy] = 1

        elif i == "D" and pos[1] > -5:
            posx = pos[0] + 5
            posy = pos[1] + 5
            pos[1] -= 1

            if sero[posx][posy] == 0:
                newline += 1
                sero[posx][posy] = 1

        print(posx,posy)

    for j in garo:
        print(j)
    for j in sero:
        print(j)
    print(newline)
    return newline

solution("LULLLLLLU")