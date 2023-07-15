# https://adventofcode.com/2016/day/11

from helper import print_result
import copy
import pathlib
import re
import sys
from collections import deque
from itertools import combinations
from typing import List, Set

DAY = 11


class Item:
    def __init__(self, element: str) -> None:
        self.element = element

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.element}>"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return repr(self) == repr(other)


class Gen(Item):
    pass


class Chip(Item):
    pass


class Floor:
    def __init__(self, generators: set, chips: set) -> None:
        self.generators = generators
        self.chips = chips

    @property
    def items(self) -> Set[Item]:
        return self.generators.union(self.chips)

    def give(self, item) -> None:
        if isinstance(item, Gen):
            self.generators.remove(item)
        else:
            self.chips.remove(item)

    def get(self, item) -> None:
        if isinstance(item, Gen):
            self.generators.add(item)
        else:
            self.chips.add(item)


class State:
    def __init__(self, elevator: int, floors: List[Floor], steps: int) -> None:
        self.elevator = elevator
        self.floors = floors
        self.steps = steps
        self.top_floor = len(floors)

    @property
    def bottom_floor(self) -> int:
        for i in range(len(self.floors)):
            if len(self.floors[i].items) > 0:
                return i

    def __repr__(self) -> str:
        res = f"[{self.steps}]:"
        for floor in self.floors:
            res += ",".join(floor.items) + "//"
        return res.rstrip("//")

    def __hash__(self):
        item_pair = {}
        for i, floor in enumerate(self.floors):
            for chip in floor.chips:
                item_pair[chip.element] = [i]
        for i, floor in enumerate(self.floors):
            for gen in floor.generators:
                item_pair[gen.element].append(i)
        return hash(str(sorted(item_pair.values())) + str(self.elevator))

    def __eq__(self, other):
        return hash(self) == hash(other)

    @property
    def is_complete(self) -> bool:
        return all(len(f.items) == 0 for f in self.floors[:-1])

    @property
    def is_valid(self) -> bool:
        for floor in self.floors:
            if floor.generators == set():
                continue
            for chip in floor.chips:
                if not any(chip.element == gen.element for gen in floor.generators):
                    return False
        return True

    def next_states(self):
        cur_floor = self.floors[self.elevator]
        for dir in [-1, 1]:
            if (
                self.elevator + dir < self.bottom_floor
                or self.elevator + dir >= self.top_floor
            ):
                continue
            for number in [1, 2]:
                for items in combinations(cur_floor.items, number):
                    state = self.generate_state(dir, items)
                    if state.is_valid:
                        yield state

    def generate_state(self, dir, items):
        new_floors = copy.deepcopy(self.floors)
        for item in items:
            new_floors[self.elevator].give(item)
            new_floors[self.elevator + dir].get(item)

        return State(
            elevator=self.elevator + dir, floors=new_floors, steps=self.steps + 1
        )


def parse(puzzle_input):
    """Parse input."""
    microchip_regex = re.compile(r"a (\w+)-compatible microchip")
    generator_regex = re.compile(r"a (\w+) generator")
    floors = []
    for line in puzzle_input.strip().splitlines():
        chips = set(Chip(s) for s in microchip_regex.findall(line))
        generators = set(Gen(s) for s in generator_regex.findall(line))
        floors.append(Floor(generators=generators, chips=chips))
    return State(elevator=0, floors=floors, steps=0)


def run(initial_state):
    """run simulation"""
    queue = deque([initial_state])
    visited = set([initial_state])

    while queue:
        state = queue.popleft()
        if state.is_complete:
            return state.steps

        for next_state in state.next_states():
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    initial_state = parse(puzzle_input)
    solution1 = run(initial_state)
    for element in ["elerium", "dilithium"]:
        initial_state.floors[0].chips.add(Chip(element))
        initial_state.floors[0].generators.add(Gen(element))
    solution2 = run(initial_state)

    return solution1, solution2


if __name__ == "__main__":
    infile = (
        sys.argv[1]
        if len(sys.argv) > 1
        else pathlib.Path(__file__).parent / f"input/day_{DAY}"
    )
    puzzle_input = pathlib.Path(infile).read_text().strip()
    p1, p2 = solve(puzzle_input)
    print_result(DAY, p1, p2)
