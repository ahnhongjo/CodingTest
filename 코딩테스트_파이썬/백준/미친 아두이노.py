def sol():
    r, c = map(int, input().split())
    game_map = []
    arduino_visit = [[0]*c for i in range(r)]
    dirs = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    crazy = []

    for i in range(r):
        game_map.append(list(input()))
        for j in range(c):
            if game_map[i][j] == 'I':
                me = [i, j]
            if game_map[i][j] == 'R':
                crazy.append([i, j])
    move_pos = list(map(int, input()))

    num =0
    for i in move_pos:
        num+=1
        me = [me[0] + dirs[i - 1][0], me[1] + dirs[i - 1][1]]

        for j in crazy:
            if not next_pos(me, j):
                print("kraj "+str(num))
                return
        if me in crazy:
            print("kraj "+str(num))
            return

        crazy = remove_dup(crazy)

    ans = [["."]*c for i in range(r)]

    ans[me[0]][me[1]] ="I"
    for i in crazy:
        ans[i[0]][i[1]] = "R"


    for i in ans:
        for j in i:
            print(j,end="")
        print()

    return


def next_pos(me, arduino):
    i = me[0] - arduino[0]
    j = me[1] - arduino[1]

    if i == 0 and j == 0:
        return False

    elif i == 0:
        arduino[1] += j // (abs(j))
    elif j == 0:
        arduino[0] += i // (abs(i))
    else:
        arduino[0] += i // (abs(i))
        arduino[1] += j // (abs(j))
    return True

def remove_dup(crazy):
    tmp =[]
    tmp_dict={}

    for i in crazy:
        a = tuple(i)
        if a in tmp_dict:
            tmp_dict[a]+=1
        else:
            tmp_dict[a]=1

    for i in tmp_dict:
        if tmp_dict[i] ==1:
            tmp.append(list(i))

    return tmp

sol()
