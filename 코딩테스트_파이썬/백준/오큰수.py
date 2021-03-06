def sol():
    cnt=int(input())
    num=list(map(int, input().split(" ")))
    answer=[]
    max_list=[0 for i in range(cnt)]
    max_list[-1]=num[-1]
    for i in range(cnt-2,-1,-1):
        if num[i]>max_list[i+1]:
            max_list[i]=num[i]
        else:
            max_list[i] = max_list[i+1]

    for i in range(len(num)-1):
        if num[i]>max_list[i+1]:
            answer.append(-1)
        else:
            for j in range(i + 1, len(num)):
                if num[i] < num[j]:
                    answer.append(num[j])
                    break

    answer.append(-1)
    for i in answer:
        print(i,end=" ")

sol()