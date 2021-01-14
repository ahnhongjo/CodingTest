def solution(n, costs):

    costs.sort(key=lambda x:x[2])
    island=[]
    for i in range(n):
        island.append(0)
    answer = 0
    cnt=0
    island_num=1
    for i in costs:

        if island[i[0]]==island[i[1]] and island[i[0]]!=0:
            continue

        elif island[i[1]]==0 and island[i[0]]==0:
            island[i[0]]=island_num
            island[i[1]]=island_num
            island_num+=1

        elif island[i[0]]==0:
            island[i[0]]=island[i[1]]

        elif island[i[1]]==0:
            island[i[1]]=island[i[0]]

        else:
            big_num=max(island[i[0]],island[i[1]])
            small_num=min(island[i[0]],island[i[1]])
            for num in range(n):
                if island[num]==big_num:
                    island[num]=small_num

        print(island)

        answer+=i[2]
        cnt+=1

        if cnt==n-1:
            break

    return answer


print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))