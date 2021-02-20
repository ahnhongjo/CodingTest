import heapq

def solution(operations):
    answer = []
    heap=[]
    for op in operations:
        if op[0]=="I":
            heap.append(int(op[2:]))

        elif op[0]=="D" and op[2]=="-":
            if len(heap)==0:
                continue
            heapq.heapify(heap)
            heapq.heappop(heap)

        else:
            tmp=[]
            if len(heap) == 0:
                continue
            for num in heap:
                heapq.heappush(tmp, (-num, num))
            heapq.heappop(tmp)

            heap = []
            for num in tmp:
                heap.append(num[1])
        print(heap)

    if len(heap)==0:
        return [0,0]
    max_tmp=[]
    heapq.heapify(heap)
    for num in heap:
        heapq.heappush(max_tmp, (-num, num))

    answer.append(heapq.heappop(max_tmp)[1])
    answer.append(heapq.heappop(heap))

    return answer
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

