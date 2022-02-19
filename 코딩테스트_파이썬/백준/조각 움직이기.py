def sol():
    board=[]
    piece=[]

    for i in range(5):
        tmp = input()
        for j in range(5):
            if tmp[j] =="*":
                piece.append((i,j))
        board.append(list(tmp))
    piece_num = len(piece)

    print(board)
    print(piece)

sol()