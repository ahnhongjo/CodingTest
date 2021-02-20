def solution(a):
    min_left = []
    min_right = [0 for i in range(len(a))]
    answer = 2

    min=a[0]
    for i in a:
        if min>i:
            min_left.append(i)
            min=i
        else:
            min_left.append(min)

    min=a[-1]
    for i in range(len(a)-1,0,-1):
        if min>a[i]:
            min_right[i]=a[i]
            min=a[i]

        else:
            min_right[i]=min

    for i in range(1,len(a)-1):
        front=min_left[i-1]
        end=min_right[i+1]
        mid=a[i]
        if front>mid and end>mid:
            answer+=1
        elif front<mid and end<mid:
            continue
        else:
            answer+=1
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))