
def solution(number, k):

    i=0
    while i < len(number) - 1:
        if number[i] < number[i + 1]:
            number=number[:i]+number[i+1:]
            k -= 1
            if i != 0:
                i -= 1

        else:
            i += 1

        if k == 0:
            break

    if k != 0:
        number = number[:len(number) - k]

    return number

print(solution("4114114111669998",3))




