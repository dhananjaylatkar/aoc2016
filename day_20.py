# https://adventofcode.com/2016/day/20

from helper import get_input, print_result
import itertools

DAY = 20

inp = get_input(DAY)


def parse_input(INP):
    res = []

    for r in INP:
        res.append([int(x) for x in r.split("-")])

    res.sort()

    return res


def merge_ranges(BIR):
    res = [BIR[0]]

    for cur in BIR:
        if res[-1][1] + 1 >= cur[0]:
            res[-1][1] = max(res[-1][1], cur[1])
        else:
            res.append(cur)

    return res


BLOCKED_IP_RANGES = merge_ranges(parse_input(inp))
MAX_IP = 4294967295


def p1():
    return BLOCKED_IP_RANGES[0][1] + 1


def p2():
    allowed_ips = 0

    for a, b in itertools.pairwise(BLOCKED_IP_RANGES):
        allowed_ips += b[0] - a[1] - 1

    if BLOCKED_IP_RANGES[-1][1] < MAX_IP:
        allowed_ips += MAX_IP - BLOCKED_IP_RANGES[-1][1] - 1

    return allowed_ips


print_result(DAY, p1(), p2())
