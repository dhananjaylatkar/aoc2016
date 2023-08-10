# https://adventofcode.com/2016/day/24

from helper import get_input, print_result

DAY = 24

inp = get_input(DAY)


class Position:
    """This will act as state of bfs at this position and current visited targets"""

    def __init__(self, x, y, visited, steps) -> None:
        self.x = x
        self.y = y
        self.visited = visited
        self.steps = steps

    def __hash__(self) -> int:
        return hash(f"{self.x}{self.y}{self.visited}")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.visited == other.visited

    def get_data(self):
        return self.x, self.y, self.visited, self.steps


def parse_input(data):
    start = (0, 0)
    open_passages = set()  # (x, y)
    targets = {}  # (x, y): val

    for x, row in enumerate(data):
        for y, val in enumerate(row):
            if val == "#":
                continue
            open_passages.add((x, y))
            if val.isdigit():
                targets[(x, y)] = int(val)
                if int(val) == 0:
                    start = (x, y)

    return start, open_passages, targets


p1_res = None
p2_res = None


def bfs():
    global p1_res
    global p2_res
    start, open_passages, targets = parse_input(inp)
    init = Position(start[0], start[1], set([]), 0)
    queue = [init]
    seen = set()
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while queue:
        cur = queue.pop(0)

        if cur in seen:
            continue

        seen.add(cur)

        x, y, visited, steps = cur.get_data()
        if (x, y) in targets:
            visited = visited | set([targets[(x, y)]])
            if len(set(visited)) == len(targets):
                if not p1_res:
                    p1_res = steps
                if (x, y) == start:
                    p2_res = steps
                    return

        for d in dirs:
            new_x, new_y = x + d[0], y + d[1]
            if (new_x, new_y) in open_passages:
                queue.append(Position(new_x, new_y, visited, steps + 1))


def p1():
    return p1_res


def p2():
    return p2_res


if __name__ == "__main__":
    bfs()
    print_result(DAY, p1(), p2())
