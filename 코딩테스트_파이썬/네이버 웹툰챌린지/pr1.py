def solution(numbers):
    answer = []
    word_nums=[]
    for i in numbers:
        word_nums.append(change_word(i))

    word_nums.sort()

    for i in word_nums:
        answer.append(change_num(i))

    return answer


def change_word(num):
    word = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight",
            "9": "nine"}
    answer = ""
    for i in str(num):
        answer += word[i]

    return answer

def change_num(num):

    nums={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

    tmp_str=""
    answer=""
    for i in num:
        tmp_str += i
        if tmp_str in nums:
            answer+=nums[tmp_str]
            tmp_str=""

    return int(answer)



solution([6,1,8])
