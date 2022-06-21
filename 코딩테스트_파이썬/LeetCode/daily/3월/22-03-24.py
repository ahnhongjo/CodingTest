from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        answer = 0
        people.sort(reverse=True)
        idx =0

        while idx <len(people):

            if people[idx] ==limit:
                answer+=1
                idx+=1

            else:
                if people[idx] + people[-1] <=limit:
                    idx+=1
                    people.pop()
                    answer+=1
                else:
                    idx+=1
                    answer+=1

        return answer



        return answer