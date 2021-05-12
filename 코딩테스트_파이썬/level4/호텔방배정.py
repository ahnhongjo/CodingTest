def solution(k, room_number):
    room = dict()
    answer = []
    for i in room_number:
        if not i in room:
            room[i] = i + 1
            answer.append(i)
        else:
            q = []
            while i in room:
                q.append(i)
                i = room[i]
            room[i] = i + 1
            for j in q:
                room[j] = i + 1
            answer.append(i)


    print(room)

    return answer


print(solution(1000,
               [1, 1, 2, 5, 6, 8, 7, 4, 2, 3, 8, 4, 2, 58, 1, 456, 58, 100, 5, 1, 0, 5, 8, 1, 3, 3, 8, 4, 1, 15, 4, 8,
                63, 2, 1]))
