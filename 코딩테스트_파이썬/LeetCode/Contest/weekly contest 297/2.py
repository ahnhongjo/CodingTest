from typing import List

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        for i in range(len(grid[0])):
            dp[0][i] = grid[0][i]
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                min_num =10000
                for k in range(len(grid[0])):
                    if min_num > dp[i-1][k] + moveCost[grid[i-1][k]][j]:
                        min_num = dp[i-1][k] + moveCost[grid[i-1][k]][j]

                dp[i][j] = grid[i][j] + min_num

        return min(dp[-1])

a = Solution()

print(a.minPathCost([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]))