import sys
sys.path.insert(0, "..")

import copy

import misc


def print_seats(content):
    print()
    for line in content:
        for c in line:
            print(c, end=" ")
        print()


def count_occupied(content, x, y):
    w = len(content[0])
    h = len(content)

    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if i < 0 or i >= w or j < 0 or j >= h:
                continue
            if i == x and j == y:
                continue

            if content[j][i] == "#":
                count += 1

    return count


def apply_rules(content):
    w = len(content[0])
    h = len(content)

    new_content = copy.deepcopy(content)
    for y in range(h):
        for x in range(w):
            c = content[y][x]

            if c == ".":
                continue

            n = count_occupied(content, x, y)

            if c == "L" and n == 0:
                new_content[y][x] = "#"
            elif c == "#" and n >= 4:
                new_content[y][x] = "L"

    return new_content

def part1(content):
    new_content = apply_rules(content)
    while new_content != content:
        content = new_content
        new_content = apply_rules(content)

    count = 0
    for line in content:
        for c in line:
            if c == "#":
                count += 1

    print("# of occupied seats: {}".format(count))


def find_next_seat(content, x, y, direction):
    w = len(content[0])
    h = len(content)

    dx = direction[0]
    dy = direction[1]

    c = "."
    while c == ".":
        x = x + dx
        y = y + dy
        if x < 0 or x >= w or y < 0 or y >= h:
            return c
        c = content[y][x]

    return c


def count_occupied_2(content, x, y):
    directions = [
        [ 0, -1],  # up
        [ 1, -1],  # up right
        [ 1,  0],  # right
        [ 1,  1],  # right down
        [ 0,  1],  # down
        [-1,  1],  # down left
        [-1,  0],  # left
        [-1, -1],  # left up
    ]

    count = 0
    for direction in directions:
        c = find_next_seat(content, x, y, direction)
        if c == "#":
            count += 1

    return count


def apply_rules_2(content):
    w = len(content[0])
    h = len(content)

    new_content = copy.deepcopy(content)
    for y in range(h):
        for x in range(w):
            c = content[y][x]

            if c == ".":
                continue

            n = count_occupied_2(content, x, y)

            if c == "L" and n == 0:
                new_content[y][x] = "#"
            elif c == "#" and n >= 5:
                new_content[y][x] = "L"

    return new_content


def part2(content):
    new_content = apply_rules_2(content)
    while new_content != content:
        content = new_content
        new_content = apply_rules_2(content)

    count = 0
    for line in content:
        for c in line:
            if c == "#":
                count += 1

    print("# of occupied seats: {}".format(count))


if __name__ == "__main__":
    content = [list(line) for line in misc.read_content()]
    part1(content)
    part2(content)
