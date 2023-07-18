# https://adventofcode.com/2016/day/17

from helper import get_input, print_result
from hashlib import md5

DAY = 17

inp = get_input(DAY)
PASSCODE = inp[0]

hashes = {}

START = (3, 0)
END = (0, 3)


def is_door_open(door_code):
    return door_code in "bcdef"


def door_state(path):
    sequence = f"{PASSCODE}{path}"
    h = hashes.get(sequence)
    if not h:
        h = md5(sequence.encode("utf-8")).hexdigest().lower()[:4]
        hashes[sequence] = h
    up, down, left, right = h
    return [
        (1, 0, is_door_open(up), "U"),
        (-1, 0, is_door_open(down), "D"),
        (0, -1, is_door_open(left), "L"),
        (0, 1, is_door_open(right), "R"),
    ]


def is_pos_valid(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4


def bfs():
    queue = []
    visited = set()
    queue.append((START[0], START[1], ""))
    visited.add((START[0], START[1], ""))
    max_path_len = 0
    shortest_path = None

    while queue:
        x, y, path = queue.pop(0)
        dirs = door_state(path)

        for d in dirs:
            _x, _y, _open, dir_name = d
            _x += x
            _y += y
            _path = f"{path}{dir_name}"
            if _open and is_pos_valid(_x, _y) and (_x, _y, _path) not in visited:
                if (_x, _y) == END:
                    if not shortest_path:
                        shortest_path = _path
                    max_path_len = max(max_path_len, len(_path))
                    continue

                visited.add((_x, _y, _path))
                queue.append((_x, _y, _path))

    return shortest_path, max_path_len


p1, p2 = bfs()

print_result(DAY, p1, p2)
