import sys
sys.path.insert(0, "..")

import misc


def parse_lines(lines):
    cl = []
    for line in lines:
        values = line.split()
        minimum, maximum = values[0].split("-")
        c = [int(minimum), int(maximum), values[1][0], values[2]]
        cl.append(c)
    return cl

def count(content, condition):
    count = 0
    for c in content:
        if condition(c):
            count += 1
    print("# valid passwords: {}".format(count))


def part1_condition(c):
    minimum, maximum, char, password = c
    count = password.count(char)
    return minimum <= count <= maximum


def part1(content):
    count(content, part1_condition)


def part2_condition(c):
    index1, index2, char, password = c
    l = len(password)
    if index1 > l or index2 > l:
        return False
    return (password[index1 - 1] == char) ^ (password[index2 - 1] == char)


def part2(content):
    count(content, part2_condition)


if __name__ == "__main__":
    content = parse_lines(misc.read_content())
    part1(content)
    part2(content)