def sol():
    n, k = map(int,input().split())

    chess_map=[]
    piece_dir =[0]
    piece_pos=[[]]
    piece_in_one =[[i] for i in range(n+1) ]
    print(piece_in_one)
    arrow = [[0,1],
             [0,-1],
             [-1,0],
             [1,0]]

    chess_map.append([0]*(n+1))
    for _ in range(n):
        chess_map.append([0]+list(map(int,(input().split()))))

    for _ in range(k):
        xi, yi, dir = map(int,input().split())
        chess_map[xi][yi] += len(piece_pos) * 10
        piece_pos.append([xi,yi])
        piece_dir.append(dir)

    #게임시작
    for game_num in range(1000):
        for i in chess_map:
            print(i)
        print()

        for i in range(1,k+1):
            if piece_in_one[i][0] == 0:
                continue

            now_pos = piece_pos[i]
            dir_num = piece_dir[i]
            move_pos=[now_pos[0]+arrow[dir_num][0],now_pos[1]+arrow[dir_num][1]]

            #범위를 벗어날때
            if move_pos[0]<= 0 or move_pos[0]>=n or move_pos[1]<=0 or move_pos[1]>=n:
                continue

            #움직인 칸이 파랑색일때
            #옷파랑색사고싶다
            if chess_map[move_pos[0]][move_pos[1]] == 2:
                if dir_num %2 ==0:
                    piece_dir[i] = dir_num-1
                else:
                    piece_dir[i] = dir_num+1
                move_pos = [now_pos[0] + arrow[dir_num], now_pos[1] + arrow[dir_num]]
                #또파랑
                if chess_map[move_pos[0]][move_pos[1]] == 2:
                    continue

            map_value = chess_map[move_pos[0]][move_pos[1]]
            map_piece = map_value//10
            map_color = map_value % 10

            if map_color ==0:
                if map_piece ==0:
                    chess_map[move_pos[0]][move_pos[1]] = i*10
                    chess_map[now_pos[0]][now_pos[1]] = chess_map[now_pos[0]][now_pos[1]] %10
                    piece_pos[i] = [move_pos[0],move_pos[1]]
                else:
                    chess_map[now_pos[0]][now_pos[1]] = chess_map[now_pos[0]][now_pos[1]] %10
                    piece_in_one[map_piece] = piece_in_one[map_piece] + piece_in_one[i]
                    piece_in_one[i] =[0]
                    piece_pos[i] = []
            
            elif map_color == 1:
                if map_piece ==0:
                    reverse_piece = piece_in_one[i][-1]
                    chess_map[move_pos[0]][move_pos[1]] = reverse_piece*10+1
                    chess_map[now_pos[0]][now_pos[1]] = chess_map[now_pos[0]][now_pos[1]] %10
                    piece_pos[i] = []
                    piece_pos[reverse_piece] = [move_pos[0],move_pos[1]]
                    piece_in_one[reverse_piece] = piece_in_one[i].reverse()
                    piece_in_one[i] =[0]

                else:
                    reverse_piece = piece_in_one[i][-1]
                    chess_map[now_pos[0]][now_pos[1]] = chess_map[now_pos[0]][now_pos[1]] %10
                    piece_pos[i] = []
                    piece_in_one[map_piece] =piece_in_one[map_piece] + piece_in_one[i].reverse()
                    piece_in_one[i] =[0]

    
            if len(piece_in_one[map_piece]) >=4:
                print(game_num)
                return



    print(-1)
    return

sol()
