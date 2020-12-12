def solution(nums):

    monster={}

    for i in nums:
        if i in monster:
            monster[i]+=1
        else:
            monster[i]=1

    if len(monster)>len(nums)/2:
        return len(nums)//2
    else:
        return len(monster)


print(solution([3,3,3,2,2,2]))