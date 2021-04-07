def sol():
    start=int(input())
    end=int(input())

    sum_value=0
    min_value=0
    min_check=True

    for i in range(start,end+1):
        if is_prime(i):
            sum_value+=i
            if min_check:
                min_value=i
                min_check=False

    if sum_value==0:
        print(-1)
    else:
        print(sum_value)
        print(min_value)

def is_prime(num):

    n=2
    while n*n<=num:
        if num%n==0:
            return False
        n+=1
    return True

sol()