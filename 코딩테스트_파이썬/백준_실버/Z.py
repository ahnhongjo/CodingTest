def sol():
    offset=[[0,1],
            [2,3]]
    answer = 0
    n, r, c = map(int,input().split(" "))

    for i in range(n, 0, -1):
        answer = answer+offset[r//pow(2,i-1)][c//pow(2,i-1)]*pow(pow(2,i-1),2)
        r = r % pow(2, i-1)
        c = c % pow(2, i - 1)

    print(answer)

sol()