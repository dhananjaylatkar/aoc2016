def get_input(day, no_strip=False):
    inp = []

    with open(f"input/day_{0 if day < 10 else ''}{day}", "r") as f:
        inp = f.readlines()

    if no_strip:
        return inp
    return [x.strip() for x in inp]


def get_input_split(day, sep=" ", strip=False):
    """
    Split input
    """

    inp = []

    with open(f"input/day_{0 if day < 10 else ''}{day}", "r") as f:
        inp = f.read().split(sep)

    return [x.strip() for x in inp] if strip else inp


def print_result(day, part1_sol, part2_sol):
    day = f"D{0 if day < 10 else ''}{day}"
    print(f"{day}P1: {part1_sol}")
    print(f"{day}P2: {part2_sol}")
