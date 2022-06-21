from typing import List

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        weights = [[int(1e10) for i in range(n)]for j in range(n)]

        for edge in edges:
            weights[edge[0]][edge[1]] = min(weights[edge[0]][edge[1]], edge[2])

        for m in range(n):
            for s in range(n):
                for d in range(n):
                    if s==d:
                        weights[s][d] =0
                    else:
                        weights[s][d] = min(weights[s][d], weights[s][m]+weights[m][d])


        if weights[src1][dest] ==int(1e10):
            return -1
        if weights[src2][dest] ==int(1e10):
            return -1

        ans = int(1e10)

        for i in range(n):
            ans = min(ans, weights[src1][i]+weights[src2][i]+weights[i][dest])

a = Solution()
a.minimumWeight(5,
[[4,2,20],[4,3,46],[0,1,15],[0,1,43],[0,1,32],[3,1,13]],
0,
4,
1)