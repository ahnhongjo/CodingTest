from typing import List
from itertools import combinations

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        idea_set = set(ideas)
        num = 0

        for idea1, idea2 in combinations(ideas,2):
            tmp = idea1[0]
            idea1 = idea2[0] + idea1[1:]
            idea2 = tmp + idea2[1:]

            if idea1 in idea_set:
                continue
            if idea2 in idea_set:
                continue

            num+=1

        return num*2


a = Solution()

print(a.distinctNames(["coffee","donuts","time","toffee"]))
