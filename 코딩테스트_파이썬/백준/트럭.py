def solution():
    n, bridge_length, weight = map(int, input().split())
    truck_weights = list(map(int, input().split()))
    bridge = [0 for i in range(bridge_length)]
    second = 0

    while True:
        if len(truck_weights) == 0 and sum(bridge) == 0:
            break
        del bridge[0]

        if len(truck_weights) > 0 and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            del truck_weights[0]
        else:
            bridge.append(0)

        second = second + 1
    answer = second
    print(answer)
    return


solution()
