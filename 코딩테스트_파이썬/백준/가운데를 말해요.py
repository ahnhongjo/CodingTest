def sol():
    n = int(input())
    numlist=[]

    for i in range(n):
        insert=int(input())
        position=pos(numlist,insert)
        numlist.insert(position,insert)
        print(numlist[i//2])

def pos(numlist,num):
    if len(numlist)==0 or num<numlist[0]:
        return 0
    if numlist[-1]<num:
        return len(numlist)

    front=0
    end=len(numlist)

    while True:
        if end-front==1 or end==front:
            return end
        mid = (front + end) // 2
        if numlist[mid]>num:
            end=mid
        else:
            front=mid

    return 0

sol()
