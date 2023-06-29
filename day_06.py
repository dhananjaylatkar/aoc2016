# https://adventofcode.com/2016/day/6

from helper import get_input, print_result
from collections import Counter

DAY = 6

inp = get_input(DAY)

# freq_rank: most_common = 0 and least_common is -1
def help(freq_rank):
    res = ""
    for col in zip(*[list(x) for x in inp]):
        res += Counter(col).most_common()[freq_rank][0]
    return res


def p1():
    return help(0)


def p2():
    return help(-1)


print_result(DAY, p1(), p2())
