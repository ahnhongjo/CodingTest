def sol():
    tmp = input()

    tmp = tmp.split(" ")

    problemNum = int(tmp[0])
    difficulty = int(tmp[1])
    solveTime = int(tmp[2])
    score = 0

    problemList = []

    for i in range(problemNum):
        difficultyTmp = input()
        difficultyTmp = difficultyTmp.split(" ")
        problemList.append(difficultyTmp)

    for i in problemList:
        if solveTime == 0:
            return score
        if int(i[1]) <= difficulty:
            i[0] = difficulty + 1
            score += 140
            solveTime -= 1



    for i in problemList:
        if solveTime == 0:
            return score
        if int(i[0]) <= difficulty:
            score += 100
            solveTime -= 1

    return score

print(sol())
