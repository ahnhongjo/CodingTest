def sol():
    r, c, n = map(int, input().split())
    bomb_map = []

    for _ in range(r):
        bomb_map.append(list(input()))

    if n % 2 == 0:
        for i in range(r):
            for j in range(c):
                print("O", end="")
            print()
        return

    for i in range(n // 2):
        for x in range(r):
            for y in range(c):
                if bomb_map[x][y] == "O":
                    bomb_map[x][y] = "X"
                    if x - 1 >= 0 and bomb_map[x - 1][y] == ".":
                        bomb_map[x - 1][y] = "X"
                    if x + 1 < r and bomb_map[x + 1][y] == ".":
                        bomb_map[x + 1][y] = "X"
                    if y - 1 >= 0 and bomb_map[x][y - 1] == ".":
                        bomb_map[x][y - 1] = "X"
                    if y + 1 < c and bomb_map[x][y + 1] == ".":
                        bomb_map[x][y + 1] = "X"

        for x in range(r):
            for y in range(c):
                if bomb_map[x][y] == ".":
                    bomb_map[x][y] = "O"
        for x in range(r):
            for y in range(c):
                if bomb_map[x][y] == "X":
                    bomb_map[x][y] = "."

    for i in range(r):
        for j in range(c):
            print(bomb_map[i][j], end="")
        print()


sol()