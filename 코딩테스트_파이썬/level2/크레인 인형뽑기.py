def solution(board, moves):
    bucket=[]
    answer=0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                if len(bucket)!=0 and bucket[-1]==board[j][i-1]:
                    del bucket[-1]
                    answer+=1
                else:
                    bucket.append(board[j][i-1])
                board[j][i-1]=0
                break
    print(answer*2)
    return answer*2

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])