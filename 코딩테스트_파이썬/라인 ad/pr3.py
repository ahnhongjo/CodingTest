def solution(ads):
    sorted_ads = sorted(ads, key=lambda x: (x[0], -x[1]))
    time = sorted_ads[0][0]+5
    del sorted_ads[0]
    cost=0
    wait = []

    while True:
        while len(sorted_ads)!=0 and sorted_ads[0][0] <= time:
            wait.append(sorted_ads[0])
            del sorted_ads[0]

        if len(wait)!=0:
            wait = sorted(wait, key=lambda x: -loss_cost(x, time + 5))
            cost=cost+(time-wait[0][0])*wait[0][1]
            time = time + 5
            del wait[0]

        elif len(sorted_ads)==0:
            break

        else:
            time = sorted_ads[0][0] + 5
            del sorted_ads[0]

    return cost


def loss_cost(ad, time):
    return ad[1]*(time-ad[0])


print(solution([[1, 3], [3, 2], [5, 4]]))
