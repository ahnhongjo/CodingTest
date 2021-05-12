def solution(numbers, hand):
    answer = ''
    left_pos=10
    right_pos=12

    for i in numbers:
        if i==1 or i==4 or i==7:
            answer+="L"
            left_pos=i
        elif i==3 or i==6 or i==9:
            answer+="R"
            right_pos=i

        else:
            nowhand=midhand(left_pos,right_pos,hand,i)
            answer+=nowhand

            if nowhand=="R":
                right_pos=i
            else:
                left_pos=i

    return answer

def midhand(left_pos,right_pos,hand,i):
    if i == 0:
        i = 11

    if right_pos==0:
        right_pos=11

    if left_pos==0:
        left_pos=11

    left_y=(left_pos-1)//3
    left_x=(left_pos-1)%3
    right_y=(right_pos-1)//3
    right_x = (right_pos-1) % 3
    mid_y=(i-1)//3
    mid_x=1

    left=abs(mid_x-left_x)+abs(mid_y-left_y)
    right=abs(mid_x-right_x)+abs(mid_y-right_y)

    if right<left:
        return "R"
    elif right>left:
        return "L"
    else:
        return hand[0].upper()


print(solution(	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"right"))