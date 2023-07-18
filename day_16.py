# https://adventofcode.com/2016/day/16

from typing import List
from helper import get_input, print_result

DAY = 16

inp = get_input(DAY)
DATA = inp[0]


def dragon_curve(data: str, size: int) -> List[int]:
    b = data
    b_len = len(b)

    # Invert all bits in inverted data
    # and prepend with zeroes to make it original size
    invert_mask = int("1" * b_len, 2)
    b = bin(int(b[::-1], 2) ^ invert_mask)[2:]
    b = f"{'0'*(b_len-len(b))}{b}"

    new_data = f"{data}0{b}"

    # If enough data is accumulated then return
    # expected data or recurse on new data

    if len(new_data) >= size:
        return [int(x) for x in new_data[:size]]

    return dragon_curve(new_data, size)


def checksum(data: List[int]) -> str:
    cs = [a ^ b ^ 1 for a, b in zip(data[1::2], data[0::2])]

    if len(cs) % 2 == 1:
        return "".join([str(x) for x in cs])

    return checksum(cs)


def p1():
    return checksum(dragon_curve(DATA, 272))


def p2():
    return checksum(dragon_curve(DATA, 35651584))


print_result(DAY, p1(), p2())
