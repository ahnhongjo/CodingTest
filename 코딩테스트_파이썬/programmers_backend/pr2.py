def solution(rows, columns, queries):
    answer = []
    made_matrix=[[i+columns*j for i in range(1,columns+1)]for j in range(rows)]

    for i in made_matrix:
        print(i)

    for query in queries:
        rot=[]

        for i in range(query[1]-1,query[3]):
            rot.append(made_matrix[query[0]-1][i])
        for i in range(query[0],query[2]):
            rot.append(made_matrix[i][query[3]-1])

        for i in range(query[3]-2,query[1]-2,-1):
            rot.append(made_matrix[query[2]-1][i])
        for i in range(query[2]-2,query[0]-1,-1):
            rot.append(made_matrix[i][query[1]-1])

        tmp=rot[-1]
        rot.remove(tmp)
        rot.insert(0,tmp)
        answer.append(min(rot))

        num=0
        for i in range(query[1]-1,query[3]):
            made_matrix[query[0]-1][i]=rot[num]
            num+=1
        for i in range(query[0],query[2]):
            made_matrix[i][query[3]-1]=rot[num]
            num+=1

        for i in range(query[3]-2,query[1]-2,-1):
            made_matrix[query[2]-1][i]=rot[num]
            num+=1
        for i in range(query[2]-2,query[0]-1,-1):
            made_matrix[i][query[1]-1]=rot[num]
            num+=1

    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])