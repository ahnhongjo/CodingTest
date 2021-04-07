import sys

def sol():
    input = sys.stdin.readline
    num=int(input())
    stack_list=[]
    stack_length=0
    for i in range(num):
        op=list(map(str,(input().split())))

        if op[0]=="push":
            stack_list.append(int(op[1]))
            stack_length+=1
        elif op[0] == "pop":
            if stack_length == 0:
                print(-1)
            else:
                print(stack_list[-1])
                del stack_list[-1]
                stack_length -= 1

        elif op[0] == "size":
            print(len(stack_list))

        elif op[0] == "empty":
            if stack_length == 0:
                print(1)
            else:
                print(0)

        elif op[0] == "top":
            if stack_length == 0:
                print(-1)
            else:
                print(stack_list[-1])


sol()