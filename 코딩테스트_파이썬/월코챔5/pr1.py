import math

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        n =math.floor(math.sqrt(i))
        if n*n==i:
            answer-=i
        else:
            answer+=i
    return answer


print(solution(13,17))
