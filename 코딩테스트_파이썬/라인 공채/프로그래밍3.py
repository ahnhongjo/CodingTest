def solution(enter, leave):
    room=[]
    enter_num=0
    leave_num=0
    answer = [0 for i in range(len(enter))]

    while leave_num!=len(leave):
        if enter_num<len(enter):
            for i in room:
                answer[i-1]+=1
            room.append(enter[enter_num])
            answer[enter[enter_num]-1]=len(room)-1
            enter_num+=1

        while len(room)>0 and leave[leave_num] in room:
            room.remove(leave[leave_num])
            leave_num+=1

    print(answer)
    return answer

solution([1,4,2,3],[2,1,3,4])