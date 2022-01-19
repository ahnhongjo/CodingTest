def solution(word):
    answer = 0
    moeum = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    plusnum=[781,156,31,6,1]
    n=0
    for i in word:
        answer = answer+ (moeum[i]-1)*plusnum[n]+1
        n+=1

    print(answer)
    return answer


solution("EIO")
