def sol():
    city_num = int(input())
    travel_num = int(input())

    road = []

    for _ in range(city_num):
        tmp = list(map(int,input().split()))
        road.append(tmp)

    for m in range(city_num):
        for s in range(city_num):
            for e in range(city_num):
                if road[s][m] ==1 and road[m][e] ==1:
                    road[s][e] =1

    for i in range(city_num):
        road[i][i] =1

    travel_order = list(map(int,input().split()))

    start = travel_order[0]-1

    for i in range(1,travel_num):
        if road[start][travel_order[i]-1] == 0:
            print("NO")
            return
        else:
            start = travel_order[i]-1

    print("YES")



sol()