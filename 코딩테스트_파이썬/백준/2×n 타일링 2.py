def sol():
    n=int(input())
    answer=[1,3]
    for i in range(n-2):
        answer.append((answer[-1]+2*answer[-2])%10007)

    print(answer[n-1])

sol()