# https://adventofcode.com/2016/day/3

from helper import get_input, print_result

DAY = 3

inp = get_input(DAY)


def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def p1():
    res = 0
    for t in inp:
        a, b, c = [int(x) for x in t.split()]
        res += is_triangle(a, b, c)
    return res


def p2():
    res = 0

    for i in range(0, len(inp), 3):
        a, b, c = [int(x) for x in inp[i].split()]
        d, e, f = [int(x) for x in inp[i + 1].split()]
        g, h, i = [int(x) for x in inp[i + 2].split()]
        res += is_triangle(a, d, g) + is_triangle(b, e, h) + is_triangle(c, f, i)
    return res


print_result(DAY, p1(), p2())
