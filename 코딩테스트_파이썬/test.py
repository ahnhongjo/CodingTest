def solution1(find_num,arys,idx):
    for i in range(len(idx)):
        if find_num==arys[idx[i]]:
            return i

    return -1


def solution2(array):
    num=0
    array.sort()
    while array[0]!=array[-1]:
        print(array)
        plus_num=array[-1]-array[0]
        for i in range(len(array)-1):
            array[i]+=plus_num

        num+=plus_num
        array.sort()
    print(array)
    print(num)
    return num

def solution3(array):
    num=0

    while len(array)>0:
        if array[-1] == max(array):
            array.remove(max(array))
        else:
            array.remove(max(array))
            num += 1
    return num



solution2([1,1000,10000])

