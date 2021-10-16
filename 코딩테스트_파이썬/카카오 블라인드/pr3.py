import math

def solution(fees, records):
    answer = []
    car_num=[]
    car_time={}
    car_io={}
    park={}

    for i in records:
        record=i.split()
        time = list(map(int,record[0].split(":")))

        if record[1] in car_num:

            if record[2]=="IN":
                car_io[record[1]] = time[0] * 60 + time[1]
                park[record[1]] = True

            else:
                car_time[record[1]]+=time[0] * 60 + time[1] - car_io[record[1]]
                park[record[1]]=False
        else:
            car_num.append(record[1])
            car_time[record[1]]=0
            car_io[record[1]]=time[0]*60+time[1]
            park[record[1]]=True

    for i in car_num:
        if park[i]:
            car_time[i]+=1439-car_io[i]

    car_num.sort()
    for i in car_num:
        if car_time[i]<=fees[0]:
            answer.append(fees[1])
        else:
            fee=fees[1]+math.ceil((car_time[i]-fees[0])/fees[2])*fees[3]
            answer.append(fee)

    print(answer)
    return answer

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])