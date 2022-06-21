class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        index = []

        for i in range(len(nums)):
            if nums[i] == key:
                index.append(i)

        ret = set()

        for i in range(len(nums)):
            for j in index:
                if abs(i - j) <= k:
                    ret.add(i)

        return list(ret)