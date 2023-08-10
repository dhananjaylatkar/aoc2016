# https://adventofcode.com/2016/day/25

from helper import get_input, print_result
from day_12 import Ins, InsInc, InsDec, InsCpy, InsJnz
from day_23 import InsTgl, execute_multi

DAY = 25

inp = get_input(DAY)
signal = [-1, -1]
s_idx = 0
number_of_signal_codes = 0
data = []


class InsOut(Ins):
    def __init__(self, x):
        super().__init__("out", x)

    def execute(self, regs, iptr):
        global signal
        global s_idx
        global number_of_signal_codes
        signal[s_idx] = self.get_x_val(regs)
        s_idx = not s_idx
        number_of_signal_codes += 1
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
            case "out":
                res.append(InsOut(ins[1]))
    return res


def p1():
    global data
    global signal
    global s_idx
    global number_of_signal_codes

    a = 1
    while True:
        data = parse_input(inp)
        signal = [-1, -1]
        s_idx = 0
        number_of_signal_codes = 0
        regs = {
            "a": a,
            "b": 0,
            "c": 0,
            "d": 0,
        }
        iptr = 0
        total_instructions = len(data)
        while iptr >= 0 and iptr < total_instructions:
            iptr = execute_multi(regs, iptr) or data[iptr].execute(regs, iptr)
            if data[iptr].op == "out" and -1 not in signal and sum(signal) != 1:
                # break if signal is not alternate 0 and 1
                break

            if number_of_signal_codes >= 10: # tune this number to your input
                return a
        a += 1


if __name__ == "__main__":
    print_result(DAY, p1(), "Yay!")
