# https://adventofcode.com/2016/day/2

from helper import get_input, print_result

DAY = 2

inp = get_input(DAY)

DIRS = {
    "U": (-1, 0),
    "D": (+1, 0),
    "L": (0, -1),
    "R": (0, +1),
}


def p1():
    KEYPAD = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    res = ""
    pos = (1, 1)  # Starting position

    def get_next_pos(code, curr):
        # print(code)
        for d in code:
            new_x = curr[0] + DIRS[d][0]
            new_y = curr[1] + DIRS[d][1]

            if new_x >= 0 and new_x < 3 and new_y >= 0 and new_y < 3:
                curr = (new_x, new_y)
            # print(curr, KEYPAD[curr[0]][curr[1]])
        return curr

    for code in inp:
        pos = get_next_pos(code, pos)
        res += str(KEYPAD[pos[0]][pos[1]])
    return res


def p2():
    KEYPAD = (
        (-1, -1, 1, -1, -1),
        (-1, 2, 3, 4, -1),
        (5, 6, 7, 8, 9),
        (-1, "A", "B", "C", -1),
        (-1, -1, "D", -1, -1),
    )
    res = ""
    pos = (2, 0)  # Starting position

    def get_next_pos(code, curr):
        # print(code)
        for d in code:
            new_x = curr[0] + DIRS[d][0]
            new_y = curr[1] + DIRS[d][1]

            if (
                new_x >= 0
                and new_x < 5
                and new_y >= 0
                and new_y < 5
                and KEYPAD[new_x][new_y] != -1
            ):
                curr = (new_x, new_y)
            # print(curr, KEYPAD[curr[0]][curr[1]])
        return curr

    for code in inp:
        pos = get_next_pos(code, pos)
        res += str(KEYPAD[pos[0]][pos[1]])
    return res


print_result(DAY, p1(), p2())
