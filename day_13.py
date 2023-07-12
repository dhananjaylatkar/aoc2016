# https://adventofcode.com/2016/day/13

from helper import get_input, print_result

DAY = 13

inp = get_input(DAY)

START = (1, 1)
END = (31, 39)
FAV_NUM = int(inp[0])
DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def is_empty(location):
    # Is given location empty?
    x, y = location

    magic_num = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + FAV_NUM
    ones = magic_num.bit_count()

    return not ones % 2


def p1():
    queue = []  # ((x,y), dist)
    visited = set()
    queue.append((START, 0))
    visited.add(START)

    while queue:
        cur, dist = queue.pop(0)
        dist += 1
        for d in DIR:
            new_point = (cur[0] + d[0], cur[1] + d[1])
            _x, _y = new_point
            if _x >= 0 and _y >= 0 and new_point not in visited and is_empty(new_point):
                if new_point == END:
                    # Found the END!
                    return dist

                queue.append((new_point, dist))
                visited.add(new_point)

    return -1


def p2():
    queue = []  # ((x,y), dist)
    visited = set()
    queue.append((START, 0))
    visited.add(START)

    while queue:
        cur, dist = queue.pop(0)
        dist += 1
        for d in DIR:
            new_point = (cur[0] + d[0], cur[1] + d[1])
            _x, _y = new_point
            if _x >= 0 and _y >= 0 and new_point not in visited and is_empty(new_point):
                if dist <= 50:
                    # add in queue only if dist is less than 50
                    # i.e. no need to visit >50 dist points
                    queue.append((new_point, dist))
                    visited.add(new_point)

    return len(visited)


print_result(DAY, p1(), p2())
