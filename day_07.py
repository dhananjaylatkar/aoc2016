# https://adventofcode.com/2016/day/7

from helper import get_input, print_result
import re

DAY = 7

inp = get_input(DAY)


# [{out = <words>, in = <words>}]
def parse_input():
    res = []
    for ip in inp:
        tmp = {}
        tmp["in"] = set(re.findall(r"\[(.*?)\]", ip))
        tmp["out"] = set(re.findall(r"\](.*?)\[", ip))

        # corner outside words
        if ip[0] != "[":
            tmp["out"].add(ip.split("[")[0])
        if ip[-1] != "]":
            tmp["out"].add(ip.split("]")[-1])

        res.append(tmp)

    return res


inp = parse_input()


def p1():
    res = 0

    def is_abba(word):
        for i in range(len(word) - 3):
            if word[i] != word[i + 1] and word[i : i + 2] == word[i + 3 : i + 1 : -1]:
                return True
        return False

    for ip in inp:
        in_res = True
        out_res = False

        # all words in brackets should *not* be abba
        for word in ip["in"]:
            if is_abba(word):
                in_res = False
                break

        if not in_res:
            continue

        # atleast one word ouside brackets should be abba
        for word in ip["out"]:
            if is_abba(word):
                out_res = True
                break

        res += out_res

    return res


def p2():
    res = 0

    def get_all_aba(words):
        aba_res = set()
        for word in words:
            for i in range(len(word) - 2):
                if word[i] != word[i + 1] and word[i] == word[i + 2]:
                    aba_res.add(word[i : i + 3])
        return aba_res

    def get_bab(aba):
        return aba[1] + aba[0] + aba[1]

    for ip in inp:
        all_aba = get_all_aba(ip["out"])
        all_bab = get_all_aba(ip["in"])
        for aba in all_aba:
            # one of aba should be in bab
            if get_bab(aba) in all_bab:
                res += 1
                break

    return res


print_result(DAY, p1(), p2())
