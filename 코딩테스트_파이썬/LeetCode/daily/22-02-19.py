from typing import List
import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_heap = []
        visited = []

        cnt = 0
        for i in range(len(nums)):
            tmp = set()
            i = nums[i]
            while True:
                tmp.add(i)
                if i % 2 != 0:
                    tmp.add(i*2)
                    heapq.heappush(min_heap, (i, cnt))
                    visited.append(tmp)
                    break
                i = i // 2
            cnt += 1
        max_nums = max(min_heap)[0]
        min_dev = max_nums - min_heap[0][0]
        while True:
            if min_dev > max_nums - min_heap[0][0]:
                min_dev = max_nums - min_heap[0][0]

            tmp = heapq.heappop(min_heap)

            tmp_num =tmp[0]
            tmp_visit = tmp[1]

            if tmp_num * 2 in visited[tmp_visit]:
                heapq.heappush(min_heap, (tmp_num * 2,tmp_visit))
                if max_nums < tmp_num*2:
                    max_nums = tmp_num*2
            else:
                break
        print(min_dev)
        return min_dev


a = Solution()

a.minimumDeviation([3,5])
