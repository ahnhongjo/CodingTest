def sol():
    n = int(input())

    rgb = [0,0,0]

    for i in range(n):
        tmp_rgb = []
        tmp = list(map(int,input().split(" ")))
        tmp_rgb.append(tmp[0]+min(rgb[1],rgb[2]))
        tmp_rgb.append(tmp[1] + min(rgb[0], rgb[2]))
        tmp_rgb.append(tmp[2] + min(rgb[1], rgb[0]))
        rgb = tmp_rgb

    print(min(rgb))


sol()