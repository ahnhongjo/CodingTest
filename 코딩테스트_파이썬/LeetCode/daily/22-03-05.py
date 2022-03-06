from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memoization = {}

        def memoi(nums):
            if nums in memoization:
                return memoization[nums]

            return max()



a = Solution()

a.deleteAndEarn([3,4,2])