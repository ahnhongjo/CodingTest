def solution(arr1, arr2):
    l=len(arr1)
    m=len(arr2)
    n=len(arr2[0])
    answer = [[0 for i in range(n)]for j in range(l)]
    for i in range(l):
        for j in range(n):
            tmp=0
            for k in range(m):
                tmp+=arr1[i][k]*arr2[k][j]

            answer[i][j]=tmp

    return answer

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))