import math

def sol():
    min_num, max_num = map(int,input().split())
    max_square=math.sqrt(max_num)
    power_prime=[]
    primes=[1 for i in range(int(max_square)+1)]

    for i in range(2,len(primes)):
        if primes[i] !=0:
            power_prime.append(i*i)
            tmp = i+i
            while tmp<len(primes):
                primes[tmp] =0
                tmp+=i
    numbers = [1 for i in range(max_num-min_num+1)]

    for primesq in power_prime:
        start = min_num%primesq
        if start !=0:
            start = primesq - start

        while start <=max_num-min_num:
            numbers[start] =0
            start+=primesq

    print(sum(numbers))

sol()