def solution(stones, k):
    start = 0
    end = max(stones)

    while True:
        mid = (start + end) // 2
        if check(stones, k, mid):
            start = mid
        else:
            end = mid - 1

        if start == end:
            return end

        if end - start == 1:
            if check(stones, k, end):
                return end
            else:
                return start

def check(stones, k, person_num):
    linear = 0
    for i in stones:
        if i < person_num:
            linear += 1
            if linear >= k:
                return False
        else:
            linear = 0

    return True


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
