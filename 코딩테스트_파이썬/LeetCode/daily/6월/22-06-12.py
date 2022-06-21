from typing import List
from collections import deque

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_val = 0
        now_val = 0
        numdic = dict()
        subarr = deque()
        for i in nums:
            if i in numdic:
                numdic[i] += 1
            else:
                numdic[i] = 1

            while numdic[i] >= 2:
                a = subarr.popleft()
                numdic[a] -= 1
                now_val -= a

            subarr.append(i)
            now_val += i
            if max_val < now_val:
                max_val = now_val
        return max_val