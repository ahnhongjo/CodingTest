def solution(routes):
    answer = 0

    in_min = routes[0][0]
    out_max = routes[0][1]
    for car in routes:
        if car[0] < in_min:
            in_min = car[0]
        if car[1] > out_max:
            out_max = car[1]

    while True:
        cam = [0 for i in range(out_max - in_min + 1)]

        for car in routes:
            if car[1]>30000:
                continue
            for i in range(car[0] - in_min, car[1] - in_min + 1, 1):
                cam[i] += 1

        if sum(cam) == 0:
            return answer

        max_cam = max(cam)
        cam_pos = cam.index(max_cam)

        for car in routes:
            if car[0] - in_min <= cam_pos and car[1] - in_min >= cam_pos:
                car[1] = 30001

        answer += 1

    return answer

print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
