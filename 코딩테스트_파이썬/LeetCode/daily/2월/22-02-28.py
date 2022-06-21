from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        before = nums[0]
        rangenum = [before, before]
        for i in range(1, len(nums)):
            if nums[i] - before == 1:
                rangenum[1] = nums[i]
            else:
                if rangenum[0] == rangenum[1]:
                    ret.append(str(rangenum[0]))
                else:
                    ret.append(str(rangenum[0]) + "->" + str(rangenum[1]))

                rangenum[0] = nums[i]
                rangenum[1] = nums[i]
            before = nums[i]

        if rangenum[0] == rangenum[1]:
            ret.append(str(rangenum[0]))
        else:
            ret.append(str(rangenum[0]) + "->" + str(rangenum[1]))
        return ret


a = Solution()
a.summaryRanges([0, 1, 2, 4, 5, 7])
