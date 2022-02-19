from itertools import combinations
import math

def sol():
    num = int(input())

    for _ in range(num):
        answer =-1
        tmp_num = int(input())
        point=[]
        point_num =[i for i in range(tmp_num)]
        for i in range(tmp_num):
            point.append(tuple(map(int,input().split())))

        plus_vectors = combinations(point_num,tmp_num//2)
        for plus_vector in plus_vectors:
            vec_x=0
            vec_y=0
            for i in range(tmp_num):
                if i in plus_vector:
                    vec_x+=point[i][0]
                    vec_y+=point[i][1]
                else:
                    vec_x-=point[i][0]
                    vec_y-=point[i][1]

            if answer == -1:
                answer = vec_x*vec_x + vec_y*vec_y

            if answer >vec_x*vec_x + vec_y*vec_y:
                answer= vec_x*vec_x + vec_y*vec_y
        print(math.sqrt(answer))

sol()