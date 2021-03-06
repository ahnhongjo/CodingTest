def solution(routes):
    answer = 0

    in_min = routes[0][0]
    out_max = routes[0][1]
    car_check=[True for i in range(out_max - in_min + 1)]

    for car in routes:
        if car[0] < in_min:
            in_min = car[0]
        if car[1] > out_max:
            out_max = car[1]
    car_record = [[0 for i in range(out_max - in_min + 1)] for j in range(len(routes))]
    cam=[0 for i in range(out_max - in_min + 1)]

    for car in range(len(routes)):
        for i in range(routes[car][0]-in_min,routes[car][1]-in_min+1,1):
            car_record[car][i]=1

    while True:
        for i in range(out_max - in_min + 1):
            sum_value = 0
            for j in range(len(car_record)):
                if car_check[j]:
                    sum_value += car_record[j][i]
            cam[i] = sum_value

        print(cam)
        if sum(cam) == 0:
            return answer
        max_car = max(cam)
        car_pos = cam.index(max_car)

        for i in range(len(car_record)):
            if car_record[i][car_pos] == 1:
                car_check[i] = False
        answer += 1

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
