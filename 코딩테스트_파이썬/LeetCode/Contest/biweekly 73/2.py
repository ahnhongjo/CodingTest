from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def sort_key(x):
            ret = ""
            for i in str(x):
                ret =  ret+str(mapping[int(i)])
            return int(ret)

        nums.sort(key = lambda x : sort_key(x))

        return nums

a = Solution()

a.sortJumbled([8,9,4,0,2,1,3,5,7,6],[991,338,38])

