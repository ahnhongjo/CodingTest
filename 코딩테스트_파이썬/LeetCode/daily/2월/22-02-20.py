from typing import List


def sort_key(interval):
    return interval[0], -(interval[1] - interval[0])


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        line = []

        intervals.sort(key=lambda x: sort_key(x))

        for interval in intervals:
            if len(line) == 0:
                line.append(interval)
                continue

            if line[-1] == interval[0]:
                continue
            else:
                if line[-1][1] >= interval[1]:
                    continue
                else:
                    line.append(interval)

        return len(line)


a = Solution()

a.removeCoveredIntervals([[1, 4], [3, 6], [2, 8], [2, 10]])
