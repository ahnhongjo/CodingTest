def sol():
    n = int(input())

    if n%5==0:
        print(n//5)
        return
    elif (n % 5) % 3 == 0:
        print(n // 5 + 1)
        return
    elif (((n % 5) + 5) % 3) == 0:
        print(n // 5 - 1 + ((n % 5) + 5) // 3)
        return
    elif (((n % 5) + 10) % 3) == 0:
        print(n // 5 - 2 + ((n % 5) + 10) // 3)
        return

    print(-1)
    return
sol()

