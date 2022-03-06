from typing import List
from bisect import bisect_left

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def bisect_left(begin, end):
            if begin >= end:
                return begin
            mid = begin + (end - begin) // 2
            totaltrip =0
            for i in time:
                totaltrip += mid//i
            if totaltrip <totalTrips:
                return bisect_left(mid + 1, end)
            else:
                return bisect_left(begin, mid)
        begin = 0
        end = totalTrips * min(time)
        ret = bisect_left(begin,end)

        return ret

a  = Solution()

a.minimumTime([2],1)