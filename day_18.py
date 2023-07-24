# https://adventofcode.com/2016/day/18

from helper import get_input, print_result

DAY = 18

inp = get_input(DAY)

TRAP = "^"
SAFE = "."
INITIAL_LAYER = list(inp[0])
INITIAL_LAYER.insert(0, SAFE)
INITIAL_LAYER.append(SAFE)

SAFE_SEQ = ["^^.", ".^^", "^..", "..^"]


def trap(tile):
    return tile == 0


def get_next_layer(layer):
    res = [SAFE]

    for i in range(1, len(layer) - 1):
        if f"{layer[i-1]}{layer[i]}{layer[i+1]}" in SAFE_SEQ:
            res.append(TRAP)
        else:
            res.append(SAFE)

    res.append(SAFE)
    return res


def help(rows):
    layer = INITIAL_LAYER
    safe_tiles = layer[1:-1].count(SAFE)

    for _ in range(rows - 1):
        layer = get_next_layer(layer)
        safe_tiles += layer[1:-1].count(SAFE)

    return safe_tiles


print_result(DAY, help(40), help(400000))
