def solution(n, m, x, y, queries):
    answer = -1
    queue = [(x, y)]

    for i in range(len(queries) - 1, -1, -1):
        q_len = len(queue)
        now_query = queries[i]
        for j in range(q_len):
            pos = queue.pop(0)
            pos_x = pos[0]
            pos_y = pos[1]

            if now_query[0] == 0:
                if pos_y == 0:
                    for a in range(min(now_query[1] + 1, m)):
                        queue.append((pos_x, a))
                elif pos_y + now_query[1] >= m:
                    continue
                else:
                    queue.append((pos_x, pos_y + now_query[1]))
            elif now_query[0] == 1:
                if pos_y == m - 1:
                    for a in range(min(now_query[1] + 1, m)):
                        queue.append((pos_x, pos_y - a))
                elif pos_y - now_query[1] < 0:
                    continue
                else:
                    queue.append((pos_x, pos_y - now_query[1]))
            elif now_query[0] == 2:
                if pos_x == 0:
                    for a in range(min(now_query[1] + 1, n)):
                        queue.append((a, pos_y))
                elif pos_x + now_query[1] >= n:
                    continue
                else:
                    queue.append((pos_x + now_query[1], pos_y))
            elif now_query[0] == 3:
                if pos_x == n - 1:
                    for a in range(min(now_query[1] + 1, n)):
                        queue.append((pos_x - a, pos_y))
                elif pos_x - now_query[1] < 0:
                    continue
                else:
                    queue.append((pos_x - now_query[1], pos_y))
        queue=list(set(queue))
        print(queue)
    answer=len(queue)
    print(queue)
    return answer


solution(5, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]])
