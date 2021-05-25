def sol():
    m,n=map(int,input().split())

    for i in range(m,n+1):
        if prime(i):
            print(i)

def prime(n):
    if n==1:
        return False
    tmp=2

    while tmp*tmp<=n:
        if n%tmp==0:
            return False
        tmp+=1

    return True
sol()