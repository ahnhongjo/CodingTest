# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    long_num=0
    front=0
    innum={}
    for i in A:
        if i in innum:
            innum[i]+=1
        else:
            innum[i]=1
        if len(innum)>2:
            tmp_len=0

            for j in innum.values():
                tmp_len+=j

            if long_num<tmp_len-1:
                long_num=tmp_len-1

            while len(innum)>2:
                del_num=A[front]
                innum[del_num]-=1
                if innum[del_num]==0:
                    del innum[del_num]

                front+=1

        print(innum)
    tmp_len = 0
    for j in innum.values():
        tmp_len += j

    if long_num<tmp_len:
        return tmp_len

    return long_num

print(solution([1,2,1,2,1,2,1,2,3]))