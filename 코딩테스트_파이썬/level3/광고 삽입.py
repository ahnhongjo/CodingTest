def solution(play_time, adv_time, logs):
    play_time_list = list(map(int, play_time.split(":")))
    adv_time_list = list(map(int, adv_time.split(":")))
    play_time_sec = play_time_list[0] * 3600 + play_time_list[1] * 60 + play_time_list[2]
    adv_time_sec = adv_time_list[0] * 3600 + adv_time_list[1] * 60 + adv_time_list[2]

    log_sec = []
    for log in logs:
        tmp = log.split("-")
        tmp_start_list = list(map(int, tmp[0].split(":")))
        tmp_start = tmp_start_list[0] * 3600 + tmp_start_list[1] * 60 + tmp_start_list[2]

        tmp_end_list = list(map(int, tmp[1].split(":")))
        tmp_end = tmp_end_list[0] * 3600 + tmp_end_list[1] * 60 + tmp_end_list[2]

        log_sec.append((tmp_start, tmp_end))

    max_time = 0
    max_start = 0

    for i in range(play_time_sec - adv_time_sec + 1):
        sum_time = 0
        for log in log_sec:
            start = log[0]
            end = log[1]
            if start > i + adv_time_sec or end < i:
                continue

            sum_time += adv_time_sec + (end - start) - (max(end, i + adv_time_sec) - min(start, i))

        if max_time < sum_time:
            max_start = i
            max_time = sum_time

    hh = str(max_start // 3600)

    if len(hh) == 1:
        hh = "0" + hh
    max_start %= 3600
    mm = str(max_start // 60)

    if len(mm) == 1:
        mm = "0" + mm
    max_start %= 60
    ss = str(max_start)

    if len(ss) == 1:
        ss = "0" + ss

    answer = str(hh) + ":" + str(mm) + ":" + str(ss)

    print(answer)
    return answer


solution("02:03:55", "00:14:15",
         ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"])
