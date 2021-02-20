def sol():
    inputValue=input()
    inputValue=inputValue.split(" ")

    B_time=int(inputValue[0])
    R_time=int(inputValue[1])

    B=[]
    R=[]

    for i in range(int(inputValue[2])):
        inputA=input()
        inputA=inputA.split(" ")
        time=int(inputA[0])
        pojang=inputA[1]
        num=int(inputA[2])
        if pojang=="B":
            for j in range(num):
                if len(B)==0:
                    B.append(time)
                elif B[-1]+B_time<time:
                    B.append(time)
                else:
                    B.append(B[-1]+B_time)

        else:
            for j in range(num):
                if len(R)==0:
                    R.append(time)
                elif R[-1]+R_time<time:
                    R.append(time)
                else:
                    R.append(R[-1]+R_time)

    B_pojang=[]
    R_pojang=[]

    for x in range(1,len(B)+len(R)+1):
        if len(B)==0:
            R_pojang.append(x)
        elif len(R)==0:
            B_pojang.append(x)
        elif B[0]<=R[0]:
            B_pojang.append(x)
            del B[0]
        elif B[0]>R[0]:
            R_pojang.append(x)
            del R[0]

    print(len(B_pojang))
    for i in B_pojang:
        print(i,end=" ")

    print("")

    print(len(R_pojang))
    for i in R_pojang:
        print(i, end=" ")

sol()
