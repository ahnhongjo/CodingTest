import random

def sol():
    num=set()

    for i in range(5):
        while len(num) < 6:
            num.add(random.randrange(1, 45))

        print(num)
        num=set()




sol()