def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        if frame[3] == 1:
            if frame[2] == 0:
                if frame[1] == 0:
                    answer.append([frame[0], frame[1], frame[2]])
                else:
                    if [frame[0] - 1, frame[1], 1] in answer or [frame[0], frame[1] - 1, 0] in answer or [frame[0],
                                                                                                          frame[1],
                                                                                                          1] in answer:
                        answer.append([frame[0], frame[1], frame[2]])
            else:
                if [frame[0], frame[1] - 1, 0] in answer or [frame[0] + 1, frame[1] - 1, 0] in answer or (
                        [frame[0] - 1, frame[1], 1] in answer and [frame[0] + 1, frame[1], 1] in answer):
                    answer.append([frame[0], frame[1], frame[2]])

        else:
            answer.remove([frame[0], frame[1], frame[2]])

            if not possible(answer):
                answer.append([frame[0], frame[1], frame[2]])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


def possible(answer):
    for frame in answer:
        if frame[2] == 0:
            if frame[1] == 0:
                continue
            else:
                if [frame[0] - 1, frame[1], 1] in answer or [frame[0], frame[1] - 1, 0] in answer or [frame[0],
                                                                                                      frame[1],
                                                                                                      1] in answer:
                    continue
                else:
                    return False
        else:
            if [frame[0], frame[1] - 1, 0] in answer or [frame[0] + 1, frame[1] - 1, 0] in answer or (
                    [frame[0] - 1, frame[1], 1] in answer and [frame[0] + 1, frame[1], 1] in answer):
                continue
            else:
                return False

    return True


solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
             [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
         )
