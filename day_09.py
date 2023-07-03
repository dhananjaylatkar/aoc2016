# https://adventofcode.com/2016/day/9

from helper import get_input, print_result

DAY = 9

inp = get_input(DAY)[0]


def help(encoded_str, p2=False):
    res = 0
    if not encoded_str:
        # Terminate when at the end of string
        return res

    n = len(encoded_str)

    # Keep adding 1 to res until decompress marker is found
    i = 0
    while i < n and encoded_str[i] != "(":
        res += 1
        i += 1
    if i == n:
        return res
    j = i + 1
    while encoded_str[j] != ")":
        j += 1

    # Get len and multiplier from decompress marker
    l, mul = (int(x) for x in encoded_str[i + 1 : j].split("x"))

    if p2:
        # recurse on "l" len substring to decompress
        res += mul * help(encoded_str[j + 1 : j + 1 + l], p2)
    else:
        # For p1, no need to recurse through substring
        res += mul * l

    # get len of remaining decoded substring
    res += help(encoded_str[j + 1 + l :], p2)

    return res


def p1():
    return help(inp, False)


def p2():
    return help(inp, True)


print_result(DAY, p1(), p2())
