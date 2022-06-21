from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        answer =[]
        for i in nums:
            if len(answer) ==0:
                answer.append(i)
                continue
            gcd_num = gcd(answer[-1],i)
            if gcd_num >1:
                answer[-1] = answer[-1]*i//gcd_num

                while len(answer) >1:
                    num1 = answer.pop()
                    num2 = answer.pop()
                    gcd_num = gcd(num1,num2)
                    if gcd_num >1:
                        answer.append(num1*num2//gcd_num)
                    else:
                        answer.append(num2)
                        answer.append(num1)
                        break
            else:
                answer.append(i)
        return answer

a = Solution()
a.replaceNonCoprimes([6,4,3,2,7,6,2])