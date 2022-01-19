def sol():

    num = int(input())
    expression = input()
    numstack =[]

    numdic = {}

    for i in range(num):
        numdic[chr(ord('A')+i)] = int(input())

    for i in expression:
        if i =='+' or i =='-' or i == '*' or i == '/':
            b = numstack.pop()
            a= numstack.pop()
            tmp_str = str(a) + i + str(b)
            tmp = eval(tmp_str)
            numstack.append(tmp)
        else:
            numstack.append(numdic[i])

    print("{:.2f}".format(numstack[0]))

sol()