def sol():
    num = int(input())

    nums=list(map(int,input().split()))

    nums.sort()
    print(nums[0]*nums[num-1])


sol()
