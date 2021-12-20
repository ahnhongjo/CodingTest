def sol():
    v,e = map(int,input().split())
    d = [[int(1e9) for i in range(v+1)] for j in range(v+1)]

    for _ in range(e):
        a, b = map(int,input().split())
        d[a][b]=1
        d[b][a]=1

    for m in range(1,v+1):
        for s in range(1,v+1):
            for e in range(1,v+1):
                if d[s][e] >d[s][m]+d[m][e]:
                    d[s][e] = d[s][m]+d[m][e]
    mink=[int(1e9),0]
    for i in range(1,len(d)):
        tmpsum=sum(d[i][1:])
        if tmpsum <mink[0]:
            mink[0]=tmpsum
            mink[1]=i
    print(mink[1])
sol()