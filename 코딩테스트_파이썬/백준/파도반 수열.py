def sol():

    t = int(input())
    triangle=[0,1,1,1,2,2]

    for _ in range(t):
        n = int(input())
        if len(triangle) >n:
            print(triangle[n])
        else:
            while len(triangle) <=n:
                triangle.append(triangle[-1]+triangle[-5])
            print(triangle[-1])

sol()