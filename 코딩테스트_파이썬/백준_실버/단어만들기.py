import sys

def sol():
    words = []

    while True:
        word = sys.stdin.readline().rstrip()
        if word == "-":
            break
        words.append(word)

    while True:
        tmp_answer=set()
        puzzle_board=sys.stdin.readline().rstrip()
        if puzzle_board == "#":
            return

        for i in puzzle_board:
            make_num=0
            for word in words:
                if i in word:
                    make_num += can_make(word,puzzle_board)

            tmp_answer.add((i,make_num))

        tmp_list_answer=sorted(tmp_answer, key=lambda x: (x[1], x[0]))

        min_num=tmp_list_answer[0][1]
        max_num=tmp_list_answer[-1][1]

        for i in tmp_list_answer:
            if i[1] == min_num:
                print(i[0], end="")
        print(" " + str(min_num), end=" ")

        for i in tmp_list_answer:
            if i[1] == max_num:
                print(i[0], end="")
        print(" " + str(max_num))


def can_make(word, puzzle_board):
    puzzle_dict={}

    for i in puzzle_board:
        if i in puzzle_dict:
            puzzle_dict[i] += 1
        else:
            puzzle_dict[i] = 1

    for i in word:
        if i in puzzle_dict and puzzle_dict[i]>0:
            puzzle_dict[i]-=1
            continue
        else:
            return 0
    return 1


sol()
