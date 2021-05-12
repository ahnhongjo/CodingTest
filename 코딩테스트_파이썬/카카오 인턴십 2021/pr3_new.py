def solution(n, k, cmd):
    now_table = ["O"] * n
    now_pos = k
    del_order = []

    for i in cmd:
        if i[0] == "D":
            now_pos = down(now_pos, now_table, int(i[2]))
        elif i[0] == "U":
            now_pos = up(now_pos, now_table, int(i[2]))

        elif i[0] == "C":
            now_table[now_pos] = "X"
            del_order.append(now_pos)
            now_pos = after_del(now_pos, now_table)

        elif i[0] == "Z":
            tmp=del_order.pop()
            now_table[tmp]="O"


    answer="".join(now_table)
    return answer


def down(pos, table, n):
    while n > 0:
        pos += 1
        if table[pos] == "O":
            n -= 1
    return pos


def up(pos, table, n):
    while n > 0:
        pos -= 1
        if table[pos] == "O":
            n -= 1
    return pos


def after_del(pos, table):
    tmp = pos
    while tmp+1 < len(table):
        tmp += 1
        if table[tmp] == "O":
            return tmp

    tmp = pos
    while tmp-1 >= 0:
        tmp -= 1
        if table[tmp] == "O":
            return tmp

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))