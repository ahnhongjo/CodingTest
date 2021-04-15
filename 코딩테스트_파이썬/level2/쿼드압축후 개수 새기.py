def solution(arr):
    return quad(arr)

def quad(arr):
    if len(arr) == 2:
        num_0 = 0
        num_1 = 0
        for i in arr:
            for j in i:
                if j == 0:
                    num_0 += 1
                elif j == 1:
                    num_1 += 1

        return num_0 // 4 + num_0 % 4, num_1 // 4 + num_1 % 4

    else:
        div_2 = len(arr) // 2
        q0 = []
        q1 = []
        q2 = []
        q3 = []
        for i in range(div_2):
            q0.append(arr[i][:div_2])
            q1.append(arr[i][div_2:])
            q2.append(arr[i + div_2][:div_2])
            q3.append(arr[i + div_2][div_2:])

        ret_tuple = sum_tuple(quad(q0), quad(q1), quad(q2), quad(q3))

        if ret_tuple[0] == 4 and ret_tuple[1] == 0:
            return 1, 0

        elif ret_tuple[0] == 0 and ret_tuple[1] == 4:
            return 0, 1

        else:
            return ret_tuple


def sum_tuple(q0, q1, q2, q3):
    return (q0[0] + q1[0] + q2[0] + q3[0], q0[1] + q1[1] + q2[1] + q3[1])


solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
