# https://adventofcode.com/2016/day/8

from helper import get_input, print_result

DAY = 8

inp = get_input(DAY)

# Board dimensions
N = 50
M = 6

ON = "#"
OFF = " "


class Instruction:
    def __init__(self, name, operation):
        self.name = name
        self.operation = operation

    def __repr__(self) -> str:
        return f"INS= {self.name}\nOPS= {self.operation}"

    def execute(self):
        pass


class InstructionRect(Instruction):
    def __init__(self, operation):
        super().__init__("re", operation)
        self.x, self.y = operation

    def execute(self, board):
        for i in range(self.y):
            for j in range(self.x):
                board[i][j] = ON
        return board


class InstructionRotateColumn(Instruction):
    def __init__(self, operation):
        super().__init__("rc", operation)
        self.col, self.move = operation
        self.move %= M

    def execute(self, board):
        transpose = list(zip(*board))
        curr_col = list(transpose[self.col])
        curr_col = curr_col[-self.move :] + curr_col[: -self.move]
        transpose[self.col] = curr_col
        return list([list(x) for x in zip(*transpose)])


class InstructionRotateRow(Instruction):
    def __init__(self, operation):
        super().__init__("rr", operation)
        self.row, self.move = operation
        self.move %= N

    def execute(self, board):
        curr_row = board[self.row]
        curr_row = curr_row[-self.move :] + curr_row[: -self.move]
        board[self.row] = curr_row
        return board


def parse_input():
    res = []
    for ins in inp:
        _ins = ins.split()

        match _ins[0]:
            case "rect":
                op = [int(x) for x in _ins[1].split("x")]
                res.append(InstructionRect(op))
            case "rotate":
                op = (int(_ins[2].split("=")[-1]), int(_ins[-1]))
                match _ins[1]:
                    case "column":
                        res.append(InstructionRotateColumn(op))
                    case "row":
                        res.append(InstructionRotateRow(op))
    return res


def run_all_instructions(inp):
    screen = [[OFF] * N for _ in range(M)]
    for ins in inp:
        screen = ins.execute(screen)
    return screen


def get_screen_str(screen):
    return "\n" + "\n".join(["".join(x) for x in screen])


inp = parse_input()
screen = run_all_instructions(inp)


def p1():
    return sum([x.count(ON) for x in screen])


def p2():
    return get_screen_str(screen)


print_result(DAY, p1(), p2())
