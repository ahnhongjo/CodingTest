def solution(genres, plays):
    answer = []
    num=len(genres)
    music_dic={}
    for i in range(num):
        if genres[i] in music_dic:
            music_dic[genres[i]][0]+=plays[i]
            music_dic[genres[i]][1].append((i,plays[i]))

        else:
            music_dic[genres[i]]=[plays[i]]
            music_dic[genres[i]].append(list())
            music_dic[genres[i]][1].append((i, plays[i]))

    sort_by_play=sorted(music_dic.items(),key=lambda x:-x[1][0])
    print(sort_by_play)
    for music in sort_by_play:
        music_list=music[1][1]
        sort_by_play_and_num=sorted(music_list,key=lambda x:(-x[1],x[0]))

        if len(sort_by_play_and_num)>1:
            answer.append(sort_by_play_and_num[0][0])
            answer.append(sort_by_play_and_num[1][0])
        else:
            answer.append(sort_by_play_and_num[0][0])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))