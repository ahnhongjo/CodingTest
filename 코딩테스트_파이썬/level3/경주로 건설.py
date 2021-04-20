from queue import PriorityQueue
import copy

class Node:
    def __init__(self, pos, miro):
        self.pos = pos
        self.miro = miro
        self.horizon = 0
        self.vertical = 0
        self.cost = 0

    def print_info(self):
        print("pos :", self.pos)
        print("miro")
        for i in self.miro:
            print(i)

        print()


def solution(board):
    start = Node((0, 0), board)
    cnt = 1

    que = PriorityQueue()
    que.put((len(board) * 2 - 2 + 5, 0,0, start))

    while not que.empty():

        tmp = que.get()
        tmp=tmp[3]
        tmp.print_info()
        tmp_pos = tmp.pos
        tmp_map = tmp.miro

        if tmp_pos[0] == len(board) - 1 and tmp_pos[1] == len(board) - 1:
            print(tmp.cost)
            return tmp.cost

        if tmp_pos[0] - 1 >= 0 and tmp_map[tmp_pos[0] - 1][tmp_pos[1]] == 0:
            que.put(move(-1, 0, tmp, cnt))
            cnt += 1

        if tmp_pos[0] + 1 < len(board) and tmp_map[tmp_pos[0] + 1][tmp_pos[1]] == 0:
            que.put(move(1, 0, tmp, cnt))
            cnt += 1

        if tmp_pos[1] - 1 >= 0 and tmp_map[tmp_pos[0]][tmp_pos[1] - 1] == 0:
            que.put(move(0, -1, tmp, cnt))
            cnt += 1

        if tmp_pos[1] + 1 < len(board) and tmp_map[tmp_pos[0]][tmp_pos[1] + 1] == 0:
            que.put(move(0, 1, tmp, cnt))
            cnt += 1

    answer = 0
    return answer


def move(vertical, horizon, node, cnt):
    miro_size = len(node.miro) - 1
    new_pos = (node.pos[0] + vertical, node.pos[1] + horizon)

    new_miro = copy.deepcopy(node.miro)
    new_miro[node.pos[0]][node.pos[1]] = 8

    new_node = Node(new_pos, new_miro)

    is_corner = abs((vertical + node.vertical) * (horizon + node.horizon))
    new_node.cost = node.cost + 100 + is_corner * 500
    new_node.vertical = abs(vertical)
    new_node.horizon = abs(horizon)

    ver_remain = miro_size - new_pos[0]
    hor_remain = miro_size - new_pos[1]

    if ver_remain != 0 and hor_remain != 0:
        remain = new_node.cost + (ver_remain + hor_remain) * 100 + 500

    elif ver_remain == 0:
        if new_node.vertical == 1:
            remain = new_node.cost + hor_remain * 100 + 500
        else:
            remain = new_node.cost + hor_remain * 100

    else:
        if new_node.horizon == 1:
            remain = new_node.cost + ver_remain * 100 + 500
        else:
            remain = new_node.cost + ver_remain * 100

    return remain, ver_remain + hor_remain, cnt, new_node


solution([[0,0,0],[0,0,0],[0,0,0]])
