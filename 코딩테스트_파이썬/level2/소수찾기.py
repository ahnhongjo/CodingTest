from itertools import permutations

def solution(numbers):

    answerSet=set()
    for i in range(1,len(numbers)+1):
        numList=list(permutations(numbers,i))

        for j in numList:
            num="".join(j)
            if isPrime(int(num)):
                answerSet.add(int(num))

    print(answerSet)
    answer = len(answerSet)
    return answer


def isPrime(num):
    if num==1 or num==0:
        return False
    if num == 2:
        return True
    div = 2

    while div ** 2 <= num:
        if num % div == 0:
            return False
        div = div + 1

    return True

print(solution("011"))
