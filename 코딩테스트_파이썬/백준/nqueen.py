def sol():
    num=int(input())
    answer_sheet=[]
    global answer
    answer=0
    put_queen(answer_sheet,num)
    print(answer)

def put_queen(answer_sheet,n):
    global answer
    length=len(answer_sheet)

    if length==n:
        # print(answer_sheet)
        answer+=1
        return
    next_element = [True for i in range(n)]

    cant=0

    for j in range(length):
        if next_element[answer_sheet[j]]:
            next_element[answer_sheet[j]]=False
            cant+=1

        if j+answer_sheet[j]-length>= 0 and next_element[j + answer_sheet[j] - length]:
            next_element[j + answer_sheet[j] - length]=False
            cant += 1

        if length+answer_sheet[j]-j<n and next_element[length + answer_sheet[j] - j]:
            next_element[length + answer_sheet[j] - j]=False
            cant += 1

        if cant==n:
            return

    for i in range(n):
        if next_element[i]:
            answer_sheet.append(i)
            put_queen(answer_sheet,n)
            del answer_sheet[-1]

sol()