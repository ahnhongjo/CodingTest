from typing import List
from collections import deque

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ret = 0
        answers = deque()

        for i in nums:
            for answer in range(len(answers)):
                tmp = answers.popleft()
                if len(tmp) == 1:
                    tmp.append(i)
                    answers.append(tmp)
                elif len(tmp) ==2:
                    if tmp[1]-tmp[0] == i -tmp[-1]:
                        ret+=1
                        tmp.append(i)
                        answers.append(tmp)
                else:
                    if tmp[1]-tmp[0] == i -tmp[-1]:
                        ret+=1
                        tmp.append(i)
                        answers.append(tmp)

            answers.append([i])

        return ret



a = Solution()

a.numberOfArithmeticSlices([1,2,3,4])