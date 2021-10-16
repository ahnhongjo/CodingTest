def solution(n, m, x, y, queries):
    left=y
    right=y
    up=x
    down=x

    for i in range(len(queries) - 1, -1, -1):
        query=queries[i]

        if query[0]==0:
            if left==0:
                right=min(m-1,right+query[1])
            else:
                left+=query[1]
                right=min(m-1,right+query[1])
        elif query[0]==1:
            if right==m-1:
                left=max(0,left-query[1])
            else:
                left = max(0, left - query[1])
                right =right-query[1]
        elif query[0]==2:
            if up==0:
                down=min(n-1,down+query[1])
            else:
                down = min(n - 1, down + query[1])
                up=up+query[1]
        else:
            if down == n-1:
                up=max(0,up-query[1])
            else:
                up = max(0, up - query[1])
                down = down -query[1]

        if left >right:
            return 0

        if up>down:
            return 0

    answer=(down-up+1)*(right-left+1)
    print(answer)
    return answer

solution(5, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]])