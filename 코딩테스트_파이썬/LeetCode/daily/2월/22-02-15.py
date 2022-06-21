from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = {}
        for i in nums:
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1
        for i in tmp:
            if tmp[i] == 1:
                return i
