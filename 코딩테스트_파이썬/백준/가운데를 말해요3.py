import heapq
import sys

def sol():
    input = sys.stdin.readline
    num = int(input())
    maxheap = []
    minheap = []
    minlen=0
    insert = int(input())
    heapq.heappush(maxheap, (-insert, insert))
    maxlen=1
    print(insert)

    for i in range(1, num):
        insert = int(input())

        if insert > maxheap[0][1]:
            heapq.heappush(minheap, insert)
            minlen+=1

        else:
            heapq.heappush(maxheap, (-insert, insert))
            maxlen+=1

        if maxlen<minlen:
            change_num = heapq.heappop(minheap)
            heapq.heappush(maxheap, (-change_num, change_num))
            maxlen+=1
            minlen-=1

        elif maxlen - minlen == 2:
            change_num = heapq.heappop(maxheap)
            heapq.heappush(minheap, change_num[1])
            maxlen-=1
            minlen+=1

        print(maxheap[0][1])


sol()
