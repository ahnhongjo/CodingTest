def solution(n,a,b):
    team=2
    num=1
    while True:
        if (a-1)//team ==(b-1)//team:
            print(num)
            return num

        team*=2
        num+=1

    answer = 0

    return answer

solution(8,4,7)