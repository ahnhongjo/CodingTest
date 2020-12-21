def solution(numbers):
    numlist = [[], [], [], [], [], [], [], [], [],[]]

    for i in numbers:
        pos=int(str(i)[0])
        if len(str(i))==1:
            i=i*10+i
        elif len(str(i))==3:
            i=i%100

        numlist[pos].append(i)
    print(numlist)
    answer = ''
    return answer


solution([3, 30, 34, 5, 9])