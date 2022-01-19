import copy


def sol():
    expression = list(input())
    post_order(expression)


def post_order(expression):
    while True:
        if "(" not in expression:
            break
        pos = expression.index("(")
        expression = expression[:pos] + post_order(expression[pos + 1:])

    tmp_exp = []
    skip = False
    for i in range(len(expression)):
        if skip:
            skip = False
            continue
        if expression[i] == "*" or expression[i] == "/":
            tmp = tmp_exp[-1] + expression[i + 1] + expression[i]
            tmp_exp[-1] = tmp
            skip = True
        elif expression[i] == ")":
            tmp_exp = tmp_exp + expression[i:]
            break

        else:
            tmp_exp.append(expression[i])

    expression = copy.deepcopy(tmp_exp)

    tmp_exp = []
    skip = False
    for i in range(len(expression)):
        if skip:
            skip = False
            continue
        if expression[i] == "+" or expression[i] == "-":
            tmp = tmp_exp[-1] + expression[i + 1] + expression[i]
            tmp_exp[- 1] = tmp
            skip = True
        elif expression[i] == ")":
            return tmp_exp + expression[i + 1:]

        else:
            tmp_exp.append(expression[i])
    expression = copy.deepcopy(tmp_exp)

    print(expression[0])
sol()
