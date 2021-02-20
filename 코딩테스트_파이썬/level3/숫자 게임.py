def solution(A, B):
    A.sort()
    B.sort()

    for i in range(len(A)):
        while A[i] >= B[i]:
            if B[i] == 0:
                return i
            B = B[:i] + B[i + 1:]
            B.append(0)

    answer = len(B)
    return answer

print(solution([5,1,3,7],[2,2,6,8]))