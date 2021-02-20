def sol():
    N = input()
    answer = ""

    for i in N:
        if i == "0":
            answer += "000"
        elif i == "1":
            answer += "001"
        elif i == "2":
            answer += "010"
        elif i == "3":
            answer += "011"
        elif i == "4":
            answer += "100"
        elif i == "5":
            answer += "101"
        elif i == "6":
            answer += "110"
        elif i == "7":
            answer += "111"

    print(int(answer))


sol()
