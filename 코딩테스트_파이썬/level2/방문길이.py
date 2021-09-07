def solution(dirs):
    pos = [0, 0]
    move_rec = set()

    for i in dirs:
        print(move_rec)
        if i == "L" and pos[0] > -5:
            move_rec.add((pos[0], pos[1], pos[0] - 1, pos[1]))
            move_rec.add((pos[0] - 1, pos[1], pos[0], pos[1]))
            pos[0] -= 1

        elif i == "R" and pos[0] < 5:
            move_rec.add((pos[0], pos[1], pos[0] + 1, pos[1]))
            move_rec.add((pos[0] + 1, pos[1], pos[0], pos[1]))
            pos[0] += 1

        elif i == "U" and pos[1] < 5:
            move_rec.add((pos[0], pos[1], pos[0], pos[1] + 1))
            move_rec.add((pos[0], pos[1] + 1, pos[0], pos[1]))
            pos[1] += 1

        elif i == "D" and pos[1] > -5:
            move_rec.add((pos[0], pos[1], pos[0], pos[1] - 1))
            move_rec.add((pos[0], pos[1] - 1, pos[0], pos[1]))
            pos[1] -= 1
    answer = len(move_rec)//2
    print(answer)
    return answer


solution("UDU")
