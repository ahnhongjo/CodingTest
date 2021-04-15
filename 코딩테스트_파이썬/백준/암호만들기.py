from itertools import combinations

def sol():
    l, c = map(int, input().split(" "))
    alpha = sorted(list(input().split()))

    tmp_answer=list(combinations(alpha,l))

    for i in tmp_answer:
        if is_right(i):
            print("".join(sorted(i)))

def is_right(tmp_str):
    mo = ["a", "e", "i", "o", "u"]
    mo_num=0
    ja_num=0
    for i in tmp_str:
        if i in mo:
            mo_num+=1
        else:
            ja_num+=1

    if mo_num>=1 and ja_num>=2:
        return True
    else:
        return False

sol()
