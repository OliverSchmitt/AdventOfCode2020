import sys
sys.path.insert(0, "..")

import misc


def get_id(row, column):
    return row * 8 + column


def divide_and_conquer(instructions, low, high):
    while low != high:
        instruction = instructions[0]
        instructions = instructions[1:]
        middle = (high - low) / 2.0
        if instruction == "F" or instruction == "L":
            high = low + int(middle)
        elif instruction == "B" or instruction == "R":
            low = low + int(middle + 1)
        else:
            print("Unknown instruction: {}".format(instruction))
    return low


def get_row(line):
    instructions = line[:-3]
    return divide_and_conquer(instructions, 0, 127)


def get_column(line):
    instructions = line[-3:]
    return divide_and_conquer(instructions, 0, 7)


def get_ids(content):
    ids = []
    for line in content:
        row = get_row(line)
        column = get_column(line)
        ids.append(get_id(row, column))
    return ids


def part1(ids):
    print("Highest seat ID: {}".format(max(ids)))


def part2(ids):
    for id in range(0, 128 * 8):
        if (id not in ids) and ((id - 1) in ids) and ((id + 1) in ids):
            print("Seat ID: {}".format(id))


if __name__ == "__main__":
    content = misc.read_content()
    ids = get_ids(content)
    part1(ids)
    part2(ids)
