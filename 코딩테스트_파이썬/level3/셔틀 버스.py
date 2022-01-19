def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    person_pos = 0
    now_time = "09:00"
    for i in range(n - 1):
        person_num = 0
        while person_num < m and person_pos < len(timetable) and timetable[person_pos] <= now_time:
            person_num += 1
            person_pos += 1

        now_time = time_calcul(now_time, t)

    person_num = 0
    last = []
    while person_num < m and person_pos < len(timetable) and timetable[person_pos] <= time_calcul(now_time, t):
        last.append(timetable[person_pos])
        person_num += 1
        person_pos += 1
    if len(last) ==m:
        return time_calcul(last[-1],-1)
    else:
        return now_time
    return answer


def time_calcul(now, plustime):
    hm = now.split(":")
    hh = int(hm[0]) + (int(hm[1]) + plustime) // 60
    mm = (int(hm[1]) + plustime) % 60

    if len(str(hh)) == 1:
        hh = "0" + str(hh)
    else:
        hh = str(hh)
    if len(str(mm)) == 1:
        mm = '0' + str(mm)
    else:
        mm = str(mm)

    return hh + ":" + mm


print(solution(11,1,1,	["09:10", "09:19", "10:20", "11:00"]))