# https://adventofcode.com/2016/day/10

from helper import get_input, print_result

DAY = 10

inp = get_input(DAY)

B = 0  # bots
O = 1  # output


def parse_input(instructions):
    # bot_cmds = {bot_id = ((B_or_O_bucket, id_for_low), (B_or_O_bucket, id_for_high)),...}
    _bot_cmds = {}
    # input_to_bot = [(bot_id, val),...]
    _input_to_bot = []

    _max_id = 0

    for ins in instructions:
        ins = ins.split()
        match ins[0]:
            case "value":
                _input_to_bot.append((int(ins[-1]), int(ins[1])))
                _max_id = max(_max_id, int(ins[-1]))
            case "bot":
                low_transaction = (B if ins[5] == "bot" else O, int(ins[6]))
                high_transaction = (B if ins[10] == "bot" else O, int(ins[11]))
                _bot_cmds[int(ins[1])] = (low_transaction, high_transaction)
                _max_id = max(_max_id, int(ins[1]), int(ins[6]), int(ins[11]))

    return _bot_cmds, _input_to_bot, _max_id + 1


BOT_CMDS, INPUT_TO_BOT, MAX_ID = parse_input(inp)
# 2 buckets, B: bots bucket and O: output bucket
buckets = {B: [[-1, -1] for _ in range(MAX_ID)], O: [[-1, -1] for _ in range(MAX_ID)]}

p1_res = None


def make_bot_transaction(transaction, curr_id):
    global p1_res
    if p1_res == None and buckets[B][curr_id] == [17, 61]:
        p1_res = curr_id

    # All buckets are sorted that means -1 is always 0th idx
    # So we can always replace -1 with new value.
    low_transaction, high_transaction = transaction
    l_bucket, l_id = low_transaction
    buckets[l_bucket][l_id][0] = buckets[B][curr_id][0]
    buckets[l_bucket][l_id].sort()

    h_bucket, h_id = high_transaction
    buckets[h_bucket][h_id][0] = buckets[B][curr_id][1]
    buckets[h_bucket][h_id].sort()

    # Empty current bucket
    buckets[B][curr_id] = [-1, -1]

    if l_bucket == B and buckets[l_bucket][l_id][0] != -1:  # new bot has two tickets
        make_bot_transaction(BOT_CMDS[l_id], l_id)

    if h_bucket == B and buckets[h_bucket][h_id][0] != -1:  # new bot has two tickets
        make_bot_transaction(BOT_CMDS[h_id], h_id)


def help():
    # run all instructions
    for ins in INPUT_TO_BOT:
        id, val = ins
        buckets[B][id][0] = val
        buckets[B][id].sort()

        if buckets[B][id][0] != -1:  # bot has two tickets
            make_bot_transaction(BOT_CMDS[id], id)


def p1():
    global p1_res
    return p1_res


def p2():
    return buckets[O][0][1] * buckets[O][1][1] * buckets[O][2][1]


help()
print_result(DAY, p1(), p2())
