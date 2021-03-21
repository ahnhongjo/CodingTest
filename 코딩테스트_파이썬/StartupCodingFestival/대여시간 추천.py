def sol():
    num = int(input())
    time = [0, 2359]
    for i in range(num):
        time_input = input().split(" ~ ")
        if int(time[0]) < int(time_input[0].replace(":", "")):
            time[0] = time_input[0]
        if int(time[1]) > int(time_input[1].replace(":", "")):
            time[1] = time_input[1]

    if time[1]<time[0]:
        print(-1)
    else:
        time[0]=str(time[0])
        time[1]=str(time[1])
        print(time[0][:2]+":"+time[0][2:4]+" ~ "+time[1][:2]+":"+time[1][2:4])

sol()
