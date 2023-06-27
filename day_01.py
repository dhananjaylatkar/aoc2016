from helper import get_input_split, print_result

DAY = 1

inp = get_input_split(day=1, sep=",", strip=True)

# Face directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Directions
DIRS = {"R": 0, "L": 1}
RIGHT = 0
LEFT = 1

# make_move[face_dir][dir] = (x_move, y_move, new_face_dir)
make_move = (
    ((+1, 0, EAST), (-1, 0, WEST)),
    ((0, -1, SOUTH), (0, +1, NORTH)),
    ((-1, 0, WEST), (+1, 0, EAST)),
    ((0, +1, NORTH), (0, -1, SOUTH)),
)

START_POS = [0, 0, NORTH]


def p1():
    pos = START_POS
    END_POS = ()

    for move in inp:
        dir = DIRS[move[0]]
        dist = int(move[1:])

        x, y, face = pos
        next_x, next_y, next_face = make_move[face][dir]
        next_x = x + next_x * dist
        next_y = y + next_y * dist
        pos = (next_x, next_y, next_face)
        END_POS = (next_x, next_y)

    return abs(END_POS[0]) + abs(END_POS[1])


def p2():
    pos = START_POS
    points = set()
    points.add((0, 0))
    END_POS = ()

    for move in inp:
        dir = DIRS[move[0]]
        dist = int(move[1:])

        x, y, face = pos
        next_x, next_y, next_face = make_move[face][dir]
        next_x = x + next_x * dist
        next_y = y + next_y * dist
        pos = (next_x, next_y, next_face)
        END_POS = (next_x, next_y)

        for i in range(x + 1, next_x):
            _pos = (i, y)
            if _pos in points:
                return abs(_pos[0]) + abs(_pos[1])
            points.add(_pos)

        for i in range(x - 1, next_x, -1):
            _pos = (i, y)
            if _pos in points:
                return abs(_pos[0]) + abs(_pos[1])
            points.add(_pos)

        for i in range(y + 1, next_y):
            _pos = (x, i)
            if _pos in points:
                return abs(_pos[0]) + abs(_pos[1])
            points.add(_pos)

        for i in range(y - 1, next_y, -1):
            _pos = (x, i)
            if _pos in points:
                return abs(_pos[0]) + abs(_pos[1])
            points.add(_pos)

        if END_POS in points:
            return abs(END_POS[0]) + abs(END_POS[1])
        points.add(END_POS)


print_result(DAY, p1(), p2())
