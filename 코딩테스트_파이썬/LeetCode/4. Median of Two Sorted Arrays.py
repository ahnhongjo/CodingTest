from typing import List
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        maxheap = []
        minheap = []

        sumlist =nums1+nums2
        for i in sumlist:
            if not maxheap:
                heapq.heappush(maxheap,-i)
                continue
            if -maxheap[0] <i:
                heapq.heappush(minheap,i)

                if len(maxheap) <len(minheap):
                    tmp = heapq.heappop(minheap)
                    heapq.heappush(maxheap,-tmp)

            else:
                heapq.heappush(maxheap,-i)
                if len(maxheap) -len(minheap) >=2:
                    tmp = heapq.heappop(maxheap)
                    heapq.heappush(minheap,-tmp)

        if len(sumlist) %2==0:
            return (-maxheap[0] + minheap[0])/2

        else:
            return -maxheap[0]


a = Solution()
print(a.findMedianSortedArrays([3],[-2,-1]))