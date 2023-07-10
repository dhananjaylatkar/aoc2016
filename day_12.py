# https://adventofcode.com/2016/day/12

from helper import get_input, print_result

DAY = 12

inp = get_input(DAY)


class Ins:
    def __init__(self, op, x, y=""):
        self.op = op
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.op=} {self.x=} {self.y=}"

    def get_x_val(self, regs):
        if not self.x.isdigit():
            return regs[self.x]
        return int(self.x)

    def execute(self):
        pass


class InsCpy(Ins):
    def __init__(self, x, y):
        super().__init__("cpy", x, y)

    def execute(self, regs, iptr):
        regs[self.y] = self.get_x_val(regs)
        return iptr + 1


class InsInc(Ins):
    def __init__(self, x):
        super().__init__("inc", x)

    def execute(self, regs, iptr):
        regs[self.x] += 1
        return iptr + 1


class InsDec(Ins):
    def __init__(self, x):
        super().__init__("dec", x)

    def execute(self, regs, iptr):
        regs[self.x] -= 1
        return iptr + 1


class InsJnz(Ins):
    def __init__(self, x, y):
        super().__init__("jnz", x, y)
        self.y = int(y)

    def execute(self, regs, iptr):
        if self.get_x_val(regs) != 0:
            return iptr + self.y
        return iptr + 1


def parse_input(data):
    res = []
    for ins in data:
        ins = ins.split()
        match ins[0]:
            case "cpy":
                res.append(InsCpy(ins[1], ins[2]))
            case "inc":
                res.append(InsInc(ins[1]))
            case "dec":
                res.append(InsDec(ins[1]))
            case "jnz":
                res.append(InsJnz(ins[1], ins[2]))
    return res


inp = parse_input(inp)


def help(regs):
    iptr = 0
    total_instructions = len(inp)
    while iptr >= 0 and iptr < total_instructions:
        # print(inp[iptr])
        iptr = inp[iptr].execute(regs, iptr)

    return regs["a"]


def p1():
    regs = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    return help(regs)


def p2():
    regs = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0,
    }
    return help(regs)


print_result(DAY, p1(), p2())
