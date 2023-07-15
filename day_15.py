# https://adventofcode.com/2016/day/15

from helper import get_input, print_result
import re

DAY = 15

inp = get_input(DAY)


class Disc:
    def __init__(self, level, positions, init_pos):
        self.time = 0
        self.level = level
        self.positions = positions
        self.init_pos = init_pos
        self.cur_pos = init_pos
        self.expected_pos = (
            self.positions - self.level + self.positions
        ) % self.positions

    def __repr__(self):
        tmp = ["-"] * self.positions
        tmp[self.cur_pos] = "o"
        return f"#{self.level} {self.expected_pos} {''.join(tmp)} {self.cur_pos}"

    def pos_at(self, time):
        """Position of Disc at given time"""
        self.cur_pos = (self.init_pos + time) % self.positions
        self.time = time
        return self.cur_pos


def parse_input(data):
    res = []
    longest_level = 0
    pos = 0
    regexp = re.compile(
        r"Disc #(\w+) has (\w+) positions; at time=0, it is at position (\w+)."
    )

    for level in data:
        level, positions, init_pos = [int(x) for x in re.findall(regexp, level)[0]]
        res.append(Disc(level, positions, init_pos))
        if pos < positions:
            longest_level = level
            pos = positions

    return res, longest_level - 1


def help(p2=False):
    data, longest_level = parse_input(inp)

    if p2:
        data_len = len(data)
        data.append(Disc(data_len + 1, 11, 0))

    # Only check the time at which longest level is at expected position.
    # This will reduce iterations significantly!
    ll = data[longest_level]
    time = (ll.expected_pos - ll.cur_pos + ll.positions) % ll.positions

    while not all([x.cur_pos == x.expected_pos for x in data]):
        time += ll.positions
        [x.pos_at(time) for x in data]

    return time


def p1():
    return help()


def p2():
    return help(p2=True)


print_result(DAY, p1(), p2())
