def sol():
    n=int(input())
    answer=[]
    for i in range(n):
        m,n,k=map(int,input().split())
        field = [[0 for x in range(m)]for y in range(n)]

        for a in range(k):
            x,y=map(int,input().split())
            field[y][x]=1


sol()