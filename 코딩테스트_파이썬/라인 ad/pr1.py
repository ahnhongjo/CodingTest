def solution(inputString):
    parqueue = []
    right = 0
    for i in range(len(inputString)):
        if inputString[i] == "[" or inputString[i] == "(" or inputString[i] == "{" or inputString[i] == "<":
            parqueue.append(inputString[i])

        elif inputString[i] == "]" or inputString[i] == ")" or inputString[i] == "}" or inputString[i] == ">":
            if len(parqueue) != 0 and check(inputString[i], parqueue[-1]):
                right += 1
                del parqueue[-1]
            else:
                return -1 * i

    if len(parqueue) != 0:
        return -1 * i

    return right
    answer = 0
    return answer


def check(inputString, parqueue):
    if inputString == "]" and parqueue == "[":
        return True
    if inputString == ">" and parqueue == "<":
        return True
    if inputString == "}" and parqueue == "{":
        return True
    if inputString == ")" and parqueue == "(":
        return True

    return False


print(solution("ABC)ABC"))
