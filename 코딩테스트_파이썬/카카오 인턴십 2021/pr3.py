def solution(n, k, cmd):
    now_table = ["O"] * n
    now_pos = k
    del_order = []
    pre_next_node = []
    for i in range(n):
        node = [i - 1, i + 1]
        pre_next_node.append(node)

    for i in cmd:
        print(now_table, now_pos, i)
        print(pre_next_node)
        print()
        if i[0] == "D":
            for j in range(int(i[2])):
                now_pos = pre_next_node[now_pos][1]

        elif i[0] == "U":
            for j in range(int(i[2])):
                now_pos = pre_next_node[now_pos][0]

        elif i[0] == "C":
            now_table[now_pos] = "X"
            del_order.append(now_pos)

            pre_pos = pre_next_node[now_pos][0]
            next_pos = pre_next_node[now_pos][1]

            if next_pos == n:
                now_pos = pre_pos
                pre_next_node[pre_pos][1] = n

            elif pre_pos == -1:
                now_pos = next_pos
                pre_next_node[next_pos][0] = -1

            else:
                now_pos = next_pos
                pre_next_node[next_pos][0] = pre_pos
                pre_next_node[pre_pos][1] = next_pos


        elif i[0] == "Z":
            tmp = del_order.pop()
            now_table[tmp] = "O"

            pre_pos = pre_next_node[tmp][0]
            next_pos = pre_next_node[tmp][1]

            if pre_pos == -1:
                pre_next_node[next_pos][0] = tmp

            elif next_pos == n:
                pre_next_node[pre_pos][1] = tmp

            else:
                pre_next_node[pre_pos][1] = tmp
                pre_next_node[next_pos][0] = tmp

    print(now_table, now_pos, i)
    print(pre_next_node)
    print()
    answer = "".join(now_table)
    return answer


print(solution(1, 0, ["C","Z","C","Z","C","Z","C","Z"]))
