from itertools import permutations
import math
def sol():
    num =0
    input_str=input()
    alpha ={}
    for i in input_str:
        if i in alpha:
            alpha[i] +=1
        else:
            alpha[i]=1
    if len(alpha) ==len(input_str):
        print(math.factorial(len(alpha)))
        return

    str_list = set(permutations(input_str,len(input_str)))

    while str_list:
        tmp=str_list.pop()
        if isfortune(tmp):
            num+=1

    print(num)

def isfortune(fortunestr):
    tmp = fortunestr[0]
    for i in  range(1,len(fortunestr)):
        if tmp ==fortunestr[i]:
            return False
        tmp=fortunestr[i]
    return True
sol()