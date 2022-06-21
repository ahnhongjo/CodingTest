from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k==0:
            return nums[0]
        if len(nums) ==1:
            if k %2 ==1:
                return -1
            else:
                return nums[0]
        elif len(nums) ==k:
            return max(nums[:-1])
        elif len(nums) > k:
            if k==1:
                return nums[1]
            return max(max(nums[:k-1]),nums[k])
        else:
            return max(nums)