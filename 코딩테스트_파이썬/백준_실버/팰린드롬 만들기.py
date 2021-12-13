def sol():
    input_str = input()

    if is_pal(input_str):
        print(len(input_str))
        return

    for i in range(len(input_str)):
        tmp_str = input_str
        for j in range(i, -1, -1):
            tmp_str += input_str[j]
        if is_pal(tmp_str):
            print(len(tmp_str))
            return


def is_pal(input_str):
    length = len(input_str)

    for i in range(length // 2):
        if input_str[i] != input_str[length - 1 - i]:
            return False

    return True


sol()