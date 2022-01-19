import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = []
    node_num = []
    num = 1
    pretree = []
    posttree = []

    for node in nodeinfo:
        tmp = (node[0], node[1], num)
        node_num.append(tmp)
        num += 1

    node_num.sort(key=lambda x: (-x[1], x[0]))

    pre_order(node_num, pretree)
    post_order(node_num, posttree)

    answer.append(pretree)
    answer.append(posttree)
    return answer


def pre_order(nodeinfo, pretree):
    if not nodeinfo:
        return
    root = nodeinfo[0]
    pretree.append(root[2])
    left = []
    right = []

    for i in nodeinfo[1:]:
        if i[0] > root[0]:
            right.append(i)
        else:
            left.append(i)
    pre_order(left, pretree)

    pre_order(right, pretree)


def post_order(nodeinfo, pretree):
    if not nodeinfo:
        return
    root = nodeinfo[0]

    left = []
    right = []

    for i in nodeinfo[1:]:
        if i[0] > root[0]:
            right.append(i)
        else:
            left.append(i)
    post_order(left, pretree)
    post_order(right, pretree)

    pretree.append(root[2])


solution([[5, 3]])
