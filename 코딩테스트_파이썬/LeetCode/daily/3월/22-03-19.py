class FreqStack:

    def __init__(self):
        self.stack = {}
        self.pos = 0

    def push(self, val: int) -> None:
        if val in self.stack:
            self.stack[val].append(self.pos)
        else:
            self.stack[val] = [self.pos]

        self.pos += 1

    def pop(self) -> int:
        max_num = 0
        for item in self.stack:
            if len(self.stack[item]) > 0:
                tmp_val = len(self.stack[item]) * (10 ** 5) + self.stack[item][-1]
                if max_num < tmp_val:
                    max_num = tmp_val
                    tmp = item

        self.stack[item].pop()
        return tmp


a = FreqStack()
command = ["push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
val = [[5], [7], [5], [7], [4], [5], [], [], [], []]

for i in range(len(command)):
    if command[i] == "push":
        a.push(val[i][0])
    else:
        print(a.pop())
