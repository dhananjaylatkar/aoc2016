# https://adventofcode.com/2016/day/14

from helper import get_input, print_result
from hashlib import md5
import re

DAY = 14

inp = get_input(DAY)

SALT = inp[0]
hashes = {}
hashes_2016 = {}


def get_md5(key):
    h = hashes.get(key)
    if not h:
        h = md5(key.encode("utf-8")).hexdigest().lower()
        hashes[key] = h
    return h


def get_md5_key_stretching(key):
    h_cache = hashes_2016.get(key)
    if h_cache:
        return h_cache

    h = get_md5(key)
    for _ in range(2016):
        h = get_md5(h)

    hashes_2016[key] = h
    return h


def help(md5_func):
    count = 0
    idx = 0

    while True:
        h = md5_func(f"{SALT}{idx}")
        triplet = re.findall(r"(\w)\1{2,}", h)
        if triplet:
            # print("Triplet found", idx, h)
            fives = triplet[0] * 5
            idx2 = idx + 1

            for _ in range(1000):
                if fives in md5_func(f"{SALT}{idx2}"):
                    count += 1
                    # print(f"Fives found, {idx=}, {idx2=}, {md5_func(f'{SALT}{idx2}')=}, {count=}")
                    if count == 64:
                        return idx
                    break
                idx2 += 1
        idx += 1

def p1():
    return help(get_md5)

def p2():
    return help(get_md5_key_stretching)


print_result(DAY, p1(), p2())
