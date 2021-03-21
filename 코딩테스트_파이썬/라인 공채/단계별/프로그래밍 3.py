def solution(program, flag_rules, commands):
    rule_book = {}
    answer = []
    flag_rules=sorted(flag_rules,key=lambda x:len(x.split(" ")))

    for rule in flag_rules:
        if len(rule.split(" ")) == 2:
            name, arg_type = rule.split(" ")
        elif len(rule.split(" ")) == 3:
            alias, arg_type, name = rule.split(" ")

            # 밑에 정의된 함수들을 넣어준다.
        if arg_type == "STRING":
            rule_book[name] = is_str

        elif arg_type == "STRINGS":
            rule_book[name] = is_strs

        elif arg_type == "NUMBER":
            rule_book[name] = is_num

        elif arg_type == "NUMBERS":
            rule_book[name] = is_nums

        elif arg_type == "NULL":
            rule_book[name] = is_null

        elif arg_type == "ALIAS":
            rule_book[alias] = rule_book[name]

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

def is_nums(input_data):
    for data in input_data:
        if not data.isdigit():
            return False
    return True

def is_str(input_data):
    if len(input_data)>1:
        return False
    return input_data[0].isalpha()

def is_strs(input_data):
    for data in input_data:
        if not data.isalpha():
            return False
    return True

def is_null(input_data):
    return input_data == []


def check(cmds, rule_book):
    done_func=[]
    for cmd in cmds:
        cmd = cmd.split(" ")
        if ("-" + cmd[0]) in rule_book:
            test_fun = rule_book["-" + cmd[0]]
            if test_fun in done_func:
                return False
            done_func.append(test_fun)
            if not test_fun(cmd[1:]):
                return False
        else:
            return False
    return True


solution(	"bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"])