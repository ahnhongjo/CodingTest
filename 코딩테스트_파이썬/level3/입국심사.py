def solution(n, times):
    front=0
    end=n*min(times)

    while front<=end:
        mid=(front+end)//2
        print(front,mid,end)

        check=min_time(n,times,mid)

        if check==0:
            return mid
        elif check==1:
            end=mid-1
        elif check==-1:
            front=mid+1

    return 0

def min_time(n, times, mid):
    person_num=0
    remain=1

    for time in times:
        person_num+= mid // time
        remain=remain*(mid % time)

    if person_num==n and remain==0:
        return 0
    elif person_num>=n:
        return 1
    elif person_num<n:
        return -1

print(solution(6,[7,10]))