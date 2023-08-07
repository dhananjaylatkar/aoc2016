# https://adventofcode.com/2016/day/22

from itertools import chain, permutations
from helper import get_input, print_result
from pprint import pprint

DAY = 22

inp = get_input(DAY)

X = 37
Y = 25


class Node:
    def __init__(self, x, y, size, used, avail, use_percent):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.use_percent = use_percent
        self.is_G = False

    def __repr__(self) -> str:
        return f"{self.used}/{self.size}"


def parse_input(INP):
    nodes = {}

    def node_loc(node):
        node = node.split("/")[-1].split("-")
        return int(node[1][1:]), int(node[2][1:])

    for inp in INP[2:]:
        inp = inp.split()
        x, y = node_loc(inp[0])
        size, used, avail, use_percent = [
            int(x)
            for x in (
                inp[1][:-1],
                inp[2][:-1],
                inp[3][:-1],
                inp[4][:-1],
            )
        ]
        # nodes.append(Node(x, y, size, used, avail, use_percent))
        if nodes.get(x):
            nodes[x].append(Node(x, y, size, used, avail, use_percent))
        else:
            nodes[x] = [Node(x, y, size, used, avail, use_percent)]

    return nodes


nodes = parse_input(inp)


def p1():
    res = 0

    for node_pair in permutations(chain(*nodes.values()), 2):
        n1, n2 = node_pair
        if n1.used != 0 and n1.used <= n2.avail:
            res += 1
    return res


def p2():
    # Print the grid and find solution by hand

    nodes_repr = []
    nodes_str = "\n"
    max_x = max(nodes.keys())

    empty_node = Node(0, 0, 0, 0, 0, 0)

    for col in nodes.values():
        for n in col:
            if n.used == 0:
                empty_node = n
                break

    for col in nodes.values():
        tmp = []
        for n in col:
            if (n.x, n.y) == (0, 0):
                tmp += ["S"]
            elif (n.x, n.y) == (max_x, 0):
                tmp += ["G"]
            elif n.used == 0:
                tmp += ["_"]
            elif n.used > empty_node.size:
                tmp += ["#"]
            else:
                tmp += ["."]
        nodes_repr.append(tmp)

    for x in zip(*nodes_repr):
        nodes_str += "".join(x) + "\n"

    # For my input
    # 10+22+2+22+6+(35*5)+1 = 238

    return nodes_str


print_result(DAY, p1(), p2())
