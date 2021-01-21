def solution(m, musicinfos):
    m_real = m[0]
    for i in range(1, len(m)):
        if m[i - 1] != "#" and m[i] != "#":
            m_real += "0"

        m_real += m[i]

    if m_real[-1] != "#":
        m_real += "0"

    answer_list = []
    order=0
    for music in musicinfos:
        time, after_time, name, melody = music.split(",")
        new_melody=melody[0]
        for i in range(1, len(melody)):
            if melody[i - 1] != "#" and melody[i] != "#":
                new_melody += "0"

            new_melody += melody[i]

        if new_melody[-1] != "#":
            new_melody += "0"

        repeat = (int(after_time[0:2]) - int(time[0:2])) * 60 + int(after_time[3:5]) - int(time[3:5])

        full_melody = ""
        for i in range(2*repeat):
            full_melody+=new_melody[i%len(new_melody)]

        if m_real in full_melody:
            answer = [repeat, order, name]
            answer_list.append(answer)

        order+=1

    if len(answer_list) == 0:
        return "(None)"

    answer_list = sorted(answer_list, key=lambda y: (-y[0], y[1]))

    return answer_list[0][2]


print(solution("ABC", ["12:00,12:14,HELLO,ABCDEF", "13:00,13:14,WORLD,ABCDEF"]))
