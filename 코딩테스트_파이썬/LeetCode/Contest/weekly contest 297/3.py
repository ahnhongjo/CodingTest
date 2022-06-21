from typing import List
from itertools import product

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_val = sum(cookies)
        if len(cookies) == k:
            return max(cookies)
        slice = [i for i in range(k)]

        for i in product(slice,repeat = len(cookies)):
            print(i)
            unfair = [0] * k
            for person in range(len(i)):
                unfair[i[person]] += cookies[person]
            min_val = min(max(unfair),min_val)
            print(unfair)

        return min_val


a = Solution()

a.distributeCookies([8,15,10,20,8],2)
