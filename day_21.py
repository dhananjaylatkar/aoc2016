# https://adventofcode.com/2016/day/21

from helper import get_input, print_result

DAY = 21

inp = get_input(DAY)


class Ins:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__} {self.x} {self.y}"

    def exec(self):
        pass

    def exec_rev(self):
        pass


class SwapPos(Ins):
    def __init__(self, x, y):
        super().__init__(int(x), int(y))

    def exec(self, s):
        s[self.x], s[self.y] = s[self.y], s[self.x]
        return s

    def exec_rev(self, s):
        return self.exec(s)


class SwapLetter(Ins):
    def __init__(self, x, y):
        super().__init__(x, y)

    def exec(self, s):
        for i, char in enumerate(s):
            if char == self.x:
                s[i] = self.y
            elif char == self.y:
                s[i] = self.x
        return s

    def exec_rev(self, s):
        return self.exec(s)


class Rotate(Ins):
    def __init__(self, x, y):
        super().__init__(x, int(y))

    def exec(self, s):
        n = len(s)
        self.y = self.y % n
        if self.x == "left":
            s = s[self.y :] + s[: self.y]
        else:
            s = s[n - self.y :] + s[: n - self.y]
        return s

    def exec_rev(self, s):
        n = len(s)
        self.y = self.y % n
        if self.x == "right":
            s = s[self.y :] + s[: self.y]
        else:
            s = s[n - self.y :] + s[: n - self.y]
        return s


class RotatePos(Ins):
    def __init__(self, x, y=0):
        super().__init__(x, y)
        # i rot new_i code
        # 0 1   1     habcdefg
        # 1 2   3     ghabcdef
        # 2 3   5     fghabcde
        # 3 4   7     efghabcd
        # 4 6   2     cdefghab
        # 5 7   4     bcdefgha
        # 6 0   6     abcdefgh
        # 7 1   0     habcdefg
        self.inv_idx_map = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 0, 0: 1}

    def exec(self, s):
        n = len(s)
        i = s.index(self.x)
        rot = i + 1 + (i >= 4)
        s = s[n - rot :] + s[: n - rot]
        return s

    def exec_rev(self, s):
        i = s.index(self.x)
        rot = self.inv_idx_map[i]
        s = s[rot:] + s[:rot]
        return s


class ReversePos(Ins):
    def __init__(self, x, y):
        super().__init__(int(x), int(y))

    def exec(self, s):
        s = s[: self.x] + s[self.x : self.y + 1][::-1] + s[self.y + 1 :]
        return s

    def exec_rev(self, s):
        return self.exec(s)


class MovePos(Ins):
    def __init__(self, x, y):
        super().__init__(int(x), int(y))

    def exec(self, s):
        x_let = s[self.x]
        del s[self.x]
        s.insert(self.y, x_let)
        return s

    def exec_rev(self, s):
        y_let = s[self.y]
        del s[self.y]
        s.insert(self.x, y_let)
        return s


def parse_input(INP):
    res = []
    for ins in INP:
        ins = ins.split()

        instruction = None
        match ins[0]:
            case "swap":
                match ins[1]:
                    case "position":
                        instruction = SwapPos(ins[2], ins[5])
                    case "letter":
                        instruction = SwapLetter(ins[2], ins[5])
            case "rotate":
                match ins[1]:
                    case "left" | "right":
                        instruction = Rotate(ins[1], ins[2])
                    case "based":
                        instruction = RotatePos(ins[-1])
            case "reverse":
                instruction = ReversePos(ins[2], ins[4])
            case "move":
                instruction = MovePos(ins[2], ins[5])

        res.append(instruction)
    return res


inp = parse_input(inp)


def p1():
    s = list("abcdefgh")
    for i in inp:
        s = i.exec(s)
    return "".join(s)


def p2():
    s = list("fbgdceah")
    for i in reversed(inp):
        s = i.exec_rev(s)
    return "".join(s)


print_result(DAY, p1(), p2())
