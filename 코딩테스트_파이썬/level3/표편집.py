def solution(n, k, cmd):
    answer = ''
    table = ['O'] * n
    delete = []
    pos = k

    for i in cmd:
        if i[0] == "D":
            pos = down(pos, table, int(i[2:]))
        elif i[0] == "U":
            pos = up(pos, table, int(i[2:]))
        elif i[0] == "C":
            pos = delcol(table, pos, delete)
        elif i[0] == "Z":
            restore(table, delete)

    for i in table:
        answer += i
    return answer


def up(pos, table, n):
    while n > 0:
        pos -= 1
        if table[pos] == "O":
            n -= 1
    return pos


def down(pos, table, n):
    while n > 0:
        pos += 1
        if table[pos] == "O":
            n -= 1
    return pos


def delcol(table, pos, delete):
    table[pos] = "X"
    delete.append(pos)
    for i in range(pos, len(table)):
        if table[i] == "O":
            return i

    for i in range(pos - 1, -1, -1):
        if table[i] == "O":
            return i


def restore(table, delete):
    tmp = delete.pop()
    table[tmp] = "O"


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
