# https://adventofcode.com/2016/day/19

from helper import get_input, print_result
import collections

DAY = 19

inp = get_input(DAY)

ELFS = int(inp[0])


def p1():
    # Josephus!
    return (int(bin(ELFS)[3:], 2) << 1) | 1


def p2():
    left = collections.deque()
    right = collections.deque()

    # Split around the middle
    for i in range(1, ELFS + 1):
        if i < (ELFS // 2) + 1:
            left.append(i)
        else:
            right.append(i)

    while left and right:
        # remove from longer half
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()

        # do rotation
        right.append(left.popleft())
        left.append(right.popleft())

    return left[0]


print_result(DAY, p1(), p2())
