from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        before_bound =0

        for br in brackets:
            if income > br[0]:
                tax+= (br[0]-before_bound)*br[1]/100
            else:
                tax+=(income - before_bound)*br[1]/100
                return tax

            before_bound = br[0]

        return tax

a = Solution()

print(a.calculateTax([[1,0],[4,25],[5,50]],2))