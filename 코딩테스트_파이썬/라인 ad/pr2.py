def solution(array):
    right_stack=[]
    left_stack=[]
    answer = [-1 for i in range(len(array))]

    for i in range(len(array)):
        if len(right_stack)==0:
            right_stack.append(i)
            continue

        while len(right_stack)!=0 and array[right_stack[-1]]<array[i]:
            answer[right_stack[-1]]=i
            del right_stack[-1]

        right_stack.append(i)

    for i in range(len(array)-1,-1,-1):
        if len(left_stack)==0:
            left_stack.append(i)
            continue

        while len(left_stack)!=0 and array[left_stack[-1]]<array[i]:
            if answer[left_stack[-1]]==-1:
                answer[left_stack[-1]]=i

            elif left_stack[-1]-i==answer[left_stack[-1]]-left_stack[-1]:
                answer[left_stack[-1]]=i

            else:
                if left_stack[-1]-i<answer[left_stack[-1]]-left_stack[-1]:
                    answer[left_stack[-1]]=i

            del left_stack[-1]

        left_stack.append(i)

    return answer

print(solution([3, 5, 4, 1, 2]))