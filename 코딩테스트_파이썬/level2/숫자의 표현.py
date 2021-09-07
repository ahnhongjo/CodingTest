def solution(n):
    answer = 0
    div=1
    while True:
        if div%2==0:
            a=(n+div//2)%div
            b=(n+div//2)//div
            if b-div//2<1:
                break
            if a==0:
                print(div)
                answer+=1


        else:
            a=n%div
            b=n//div
            if b-div//2<1:
                break
            if a==0:
                print(div)
                answer+=1

        div+=1

    return answer

solution(6)