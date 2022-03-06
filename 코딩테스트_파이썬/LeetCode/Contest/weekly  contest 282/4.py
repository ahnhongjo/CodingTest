from typing import List


class Solution:
    def min_one_tire(self, tires, n):
        min_value = int(1e10)
        for tire in tires:
            if min_value > tire[0]*(tire[1]**n-1)//(tire[1]-1):
                min_value = tire[0]*(tire[1]**n-1)//(tire[1]-1)

        return min_value

    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        min_time = {}
        for i in range(1, numLaps + 1):
            min_time[i] = self.min_one_tire(tires, i)
            for j in range(1, i):
                if min_time[i] > min_time[j] + min_time[i - j] + changeTime:
                    min_time[i] = min_time[j] + min_time[i - j] + changeTime
        print(min_time[numLaps])
        return min_time[numLaps]


a = Solution()
a.minimumFinishTime([[2, 3], [3, 4]], 5,4)
