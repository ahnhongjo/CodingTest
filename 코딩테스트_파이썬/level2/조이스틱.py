def solution(name):
    sub = []
    for i in name:
        if ord(i) >= ord("N"):
            sub.append(ord("Z") + 1 - ord(i))
        else:
            sub.append(ord(i) - ord("A"))

    rightSub = [i for i in sub]
    right = 0
    rightNum = 0
    while True:
        if sum(rightSub) == 0:
            break
        if rightSub[rightNum] != 0:
            right += rightSub[rightNum]
            rightSub[rightNum] = 0
            rightNum += 1

    right += rightNum


    left = 0
    leftNum = 0

    while True:
        if sum(sub) == 0:
            break
        if sub[leftNum] != 0:
            left += sub[leftNum]
            sub[leftNum] = 0
            leftNum -= 1

    left += abs(leftNum)

    answer = min(right, left)

    return answer