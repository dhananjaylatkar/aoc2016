# https://adventofcode.com/2016/day/23

from helper import get_input, print_result
from day_12 import Ins, InsInc, InsDec, InsCpy, InsJnz

DAY = 23

inp = get_input(DAY)
N = len(inp)
data = []


class InsTgl(Ins):
    def __init__(self, x):
        super().__init__("tgl", x)

    def execute(self, regs, iptr):
        global data
        i = iptr + self.get_x_val(regs)
        if i < 0 or i >= len(data):
            return iptr + 1

        ins = data[i]
        match ins.op:
            case "inc":
                data[i] = InsDec(ins.x)
            case "dec" | "tgl":
                data[i] = InsInc(ins.x)
            case "jnz":
                data[i] = InsCpy(ins.x, ins.y)
            case "cpy":
                data[i] = InsJnz(ins.x, ins.y)

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
            case "tgl":
                res.append(InsTgl(ins[1]))
    return res


def get_val(regs, r):
    return int(r) if regs.get(r) is None else regs.get(r)


def execute_multi(regs, iptr):
    if [x.op for x in data[iptr : iptr + 6]] == [
        "cpy",
        "inc",
        "dec",
        "jnz",
        "dec",
        "jnz",
    ]:
        cpy_x, cpy_y = data[iptr].x, data[iptr].y
        inc_x = data[iptr + 1].x
        dec2_x = data[iptr + 4].x

        regs[inc_x] += get_val(regs, cpy_x) * get_val(regs, dec2_x)
        regs[cpy_y] = 0
        regs[dec2_x] = 0
        return iptr + 6

    return 0


def help(regs):
    iptr = 0
    total_instructions = len(data)
    while iptr >= 0 and iptr < total_instructions:
        iptr = execute_multi(regs, iptr) or data[iptr].execute(regs, iptr)

    return regs["a"]


def p1():
    global data
    data = parse_input(inp)
    regs = {
        "a": 7,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    return help(regs)


def p2():
    global data
    data = parse_input(inp)
    regs = {
        "a": 12,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    return help(regs)


if __name__ == "__main__":
    print_result(DAY, p1(), p2())
