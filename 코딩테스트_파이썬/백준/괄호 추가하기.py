from collections import deque
import sys

input = sys.stdin.readline

def sol():
    max_value = -(2**31)
    n = int(input())
    expression = list(input())

    q= deque()
    q.append((expression,n))

    while q:
        nownode = q.popleft()
        if nownode[1] ==1 and int(nownode[0][0]) >max_value:
            max_value = int(nownode[0][0])

        for i in range(0,nownode[1]-2,2):
            num1 = int(nownode[0][i])
            num2 = int(nownode[0][i+2])
            oper = nownode[0][i+1]

            if oper =="+":
                value = num1+num2
            elif oper == "*":
                value = num1 * num2
            elif oper =="-":
                value = num1 - num2
            tmp = (nownode[0][:i]+[value]+nownode[0][i+3:],nownode[1]-2)
            q.append(tmp)

    print(max_value)
sol()