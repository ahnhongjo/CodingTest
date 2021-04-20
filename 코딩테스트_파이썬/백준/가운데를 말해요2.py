import heapq
import sys

def sol():
    input = sys.stdin.readline
    num=int(input())
    numlist=[]
    for i in range(num):
        numlist.append(int(input()))
        print(kth_smallest(numlist,i//2))

def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    kth_min = heapq.heappop(heap)
    for _ in range(k):
        kth_min = heapq.heappop(heap)
    return kth_min

sol()