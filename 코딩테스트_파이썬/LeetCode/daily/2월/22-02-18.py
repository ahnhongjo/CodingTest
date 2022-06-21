from itertools import combinations_with_replacement
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        for i in range(1, target // min(candidates) + 1):
            for j in combinations_with_replacement(candidates, i):
                if sum(j) == target:
                    ret.append(list(j))
        return ret
