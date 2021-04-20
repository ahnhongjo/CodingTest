from queue import PriorityQueue

def sol():
    num = int(input())
    que1 = PriorityQueue()
    que2 = PriorityQueue()
    q1 = True

    for i in range(num):
        insert = int(input())
        if q1:
            que1.put(insert)
            for j in range(i + 1):
                getq1 = que1.get()
                if j == i // 2:
                    print(getq1)
                que2.put(getq1)
            q1 = False

        else:
            que2.put(insert)
            for j in range(i + 1):
                getq2 = que2.get()
                if j == i // 2:
                    print(getq2)
                que1.put(getq2)
            q1 = True

sol()
