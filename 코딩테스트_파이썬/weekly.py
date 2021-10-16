def solution(line):
    answer = []
    point = []
    for i in range(len(line) - 1):
        for j in line[i + 1:]:
            temp = get_answer(line[i], j)
            if temp and not (temp in point):
                point.append(temp)
    min_x = point[0][0]
    max_x = point[0][0]
    min_y = point[0][1]
    max_y = point[0][1]

    for i in point:
        if min_x > i[0]:
            min_x = i[0]
        if max_x < i[0]:
            max_x = i[0]
        if min_y > i[1]:
            min_y = i[1]
        if max_y < i[1]:
            max_y = i[1]

    for i in range(max_y - min_y + 1):
        temp = []
        for j in range(max_x - min_x + 1):
            temp.append(".")
        answer.append(temp)
    for i in point:
        answer[-1 * (i[1] - max_y)][(i[0] - min_x)] = "*"

    temp=[]
    for i in answer:
        temp.append("".join(i))

    print(temp)

    return temp


def get_answer(line1, line2):
    h = line1[0] * line2[1] - line1[1] * line2[0]
    if h == 0:
        return False
    else:
        x = line1[1] * line2[2] - line2[1] * line1[2]
        y = line2[0] * line1[2] - line1[0] * line2[2]

        if x / h != x // h:
            return False
        if y / h != y // h:
            return False

    return (x // h, y // h)


solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])