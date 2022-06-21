from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        plus_num = 1
        cnt = 0
        answer = 0
        numset = set(nums)

        while True:
            if cnt == k:
                return answer
            if plus_num in numset:
                plus_num += 1
                continue
            else:
                answer += plus_num
                cnt += 1
                plus_num += 1

a= Solution()
print(a.minimalKSum([1],100000000))