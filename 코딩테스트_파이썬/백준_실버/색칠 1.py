def sol():
    w, h, f, c, x1,y1, x2,y2 = map(int,input().split())

    sum =0
    min_garo= min(w-f,f)
    if x2 <=min_garo:
        sum = (x2-x1)*2*(c+1)
    elif x1>=min_garo:
        sum = (x2-x1)*(c+1)
    else:
        sum = sum + (min_garo - x1) * 2 * (c + 1)
        sum = sum + (x2 - min_garo) * (c + 1)
    sum *=(y2-y1)
    print(w*h-sum)

sol()