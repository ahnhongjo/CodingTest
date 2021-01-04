def sol():
    n = int(input())

    num = list(map(int, input().split(" ")))
    a = num[0]
    b = num[1]
    c = num[2]
    d = num[3]
    e = num[4]
    f = num[5]

    if n == 1:
        hide=max(a,b,c,d,e,f)
        print(a + b + c + d + e + f-hide)
        return

    if n == 2:
        ver = min(a + d + e, a + b + d, a + b + c, a + e + c, f + d + e, f + d + b, f + b + c, f + e + c)
        edge = min(a + d, a + e, a + b, a + c, b + d, b + f, b + c, e + d, e + c, f + d, f + c, f + e)
        print(4 * ver+4*edge)
        return

    edge = min(a + d, a + e, a + b, a + c, b + d, b + f, b + c, e + d, e + c, f + d, f + c, f + e)
    ver = min(a + d + e, a + b + d, a + b + c, a + e + c, f + d + e, f + d + b, f + b + c, f + e + c)
    face = min(a, b, c, d, e, f)

    print(4 * face * (n - 2)*(n - 1)+face * (n - 2)*(n - 2) + 4 * ver + (8*n - 12) * edge)

sol()
