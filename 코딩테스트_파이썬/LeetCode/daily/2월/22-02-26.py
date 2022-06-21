from typing import List
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        short_path = 2*len(graph)

        for start in range(len(graph)):
            q = deque()
            visited = 0 | 1<<(start)
            q.append((start,visited,0))

            while True:
                now = q.popleft()
                if now[1] ==(2**len(graph))-1:
                    if short_path > now[2]:
                        short_path = now[2]
                    break

                for i in graph[now[0]]:
                    q.append((i,now[1] | 1<<i,now[2]+1))
        return short_path





test = Solution()
test.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])
