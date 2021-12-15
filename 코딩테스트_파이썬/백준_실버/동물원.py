def sol():
    n = int(input())
    zoo=[[0,1],[0,2]]
    for i in range(2,n+1):
        zoo[0].append((zoo[0][i-1]+zoo[1][i-1])%9901)
        zoo[1].append((zoo[1][i-1]+2*zoo[0][i-1])%9901)

    print((zoo[0][n]+zoo[1][n])%9901)

sol()