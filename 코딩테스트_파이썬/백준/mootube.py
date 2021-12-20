from collections import deque

def sol():
    n, q = map(int,input().split())
    usado = [[]for i in range(n+1)]

    for _ in range(n-1):
        pi, qi, ri = map(int,input().split())
        usado[pi].append((qi,ri))
        usado[qi].append((pi,ri))

    answersheet=set()
    answer={}
    for _ in range(q):
        k, v = map(int,input().split())

        if (k,v) in answersheet:
            print(answer[(k,v)])

        else:
            q = deque()
            q.append((v, int(1e9)))
            visited = set()

            num = -1

            while q:
                nownode = q.popleft()
                if nownode[1] >= k:
                    num += 1
                visited.add(nownode[0])
                for i in usado[nownode[0]]:
                    if i[0] not in visited:
                        q.append((i[0], min(i[1], nownode[1])))

            answersheet.add((k,v))
            answer[(k,v)]=num
            print(num)


sol()