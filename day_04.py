# https://adventofcode.com/2016/day/4

from helper import get_input, print_result
from collections import Counter

DAY = 4

inp = get_input(DAY)


# Parse input
# (room_code, sector_id, checksum)
def parse_input():
    res = []
    for room in inp:
        room = room.split("-")
        tmp = room[-1].split("[")
        sector_id = int(tmp[0])
        checksum = tmp[1][:-1]
        res.append((room[:-1], sector_id, checksum))
    return res


inp = parse_input()
real_rooms = []


def p1():
    res = 0
    for r in inp:
        top_5 = Counter(sorted("".join(r[0]))).most_common(5)
        top_5 = "".join(x[0] for x in top_5)
        if top_5 == r[2]:
            res += r[1]
            real_rooms.append(r)
    return res


def p2():
    def get_room_name(rc, rot):
        res = ""
        for room_code in rc:
            for r in room_code:
                res += chr(((ord(r) - 97 + rot) % 26) + 97)
            res += " "
        return res.strip()

    for room in real_rooms:
        rc, rot, _ = room
        if get_room_name(rc, rot) == "northpole object storage":
            return rot


print_result(DAY, p1(), p2())
