# https://adventofcode.com/2016/day/5

from helper import get_input, print_result
from hashlib import md5

DAY = 5

inp = get_input(DAY)[0]


def p1():
    res = ""
    count = 0

    def get_next_char(door_id, count):
        while True:
            h = md5(f"{door_id}{count}".encode("utf-8")).hexdigest()
            if h[:5] == "00000":
                return h[5], count + 1
            count += 1

    for _ in range(8):
        ch, count = get_next_char(inp, count)
        res += ch
    return res


def p2():
    res = [""] * 8
    count = 0

    def get_next_char(door_id, count):
        while True:
            h = md5(f"{door_id}{count}".encode("utf-8")).hexdigest()
            if h[:5] == "00000" and h[5] >= "0" and h[5] < "8":
                return int(h[5]), h[6], count + 1
            count += 1

    while res.count(""):
        idx, ch, count = get_next_char(inp, count)
        if res[idx] == "":
            res[idx] = ch
    return "".join(res)


print_result(DAY, p1(), p2())
