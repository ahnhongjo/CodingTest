def sol():
    n,k = map(int,input().split())
    coin =[]
    answer=[0]*(k+1)
    answer[0]=1

    for _ in range(n):
        tmp = int(input())
        coin.append(tmp)
    coin.sort()

    for i in coin:
        for j in range(i,k+1):
            answer[j] +=answer[j-i]


    print(answer[-1])
sol()