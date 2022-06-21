from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        nums_dict={}
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] in nums_dict:
                    nums_dict[nums[i+1]] +=1
                else:
                    nums_dict[nums[i+1]]=1

        max_cnt =0
        max_num =0
        for i in nums_dict.items():
            if i[1] > max_cnt:
                max_num = i[0]
                max_cnt= i[1]
        return max_num

a = Solution()
a.mostFrequent([2,2,2,2,3],2)

