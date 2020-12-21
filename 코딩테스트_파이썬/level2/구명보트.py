def solution(people, limit):
    answer = 0

    people.sort(reverse=True)

    for j in range(len(people)):
        if people[j]==0:
            continue
        elif people[j]>limit-40:
            people[j]=0
            answer+=1
            continue
        else:
            boat=people[j]

        for i in range(j+1,len(people)):
            if people[i]==0:
                continue

            if boat+people[i]>limit:
                continue
            elif boat+people[i]>limit-40:
                boat = boat + people[i]
                people[i]=0
                break
            else:
                boat=boat+people[i]
                people[i]=0

        answer=answer+1

    return answer


people=	[40,40,40,40,40]
limit=45
print(solution(people,limit))
