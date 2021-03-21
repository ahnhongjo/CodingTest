def solution(program, flag_rules, commands):
    rule_book = {}
    answer = []

    for rule in flag_rules:
        name, arg_type = rule.split(" ")

        #밑에 정의된 함수들을 넣어준다.
        if arg_type == "STRING":
            rule_book[name] = is_str

        elif arg_type == "NUMBER":
            rule_book[name] = is_num

        elif arg_type == "NULL":
            rule_book[name] = is_null

    for cmd in commands:
        cmd = cmd.split(" -")

        if cmd[0] != program:
            answer.append(False)
        else:
            answer.append(check(cmd[1:], rule_book))
    return answer


# check command_input
def is_num(input_data):
    if len(input_data)>1:
        return False
    input_data = str(input_data[0])
    return input_data.isdigit()

def is_str(input_data):
    if len(input_data)>1:
        return False
    return input_data[0].isalpha()

def is_null(input_data):
    return input_data == []


def check(cmds, rule_book):
    for cmd in cmds:
        cmd=cmd.split(" ")
        if ("-" + cmd[0]) in rule_book:
            test_fun = rule_book["-" + cmd[0]]
            if not test_fun(cmd[1:]):
                return False
        else:
            return False
    return True