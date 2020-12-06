import sys
sys.path.insert(0, "..")

import re

import misc


REGEX = {
    "byr": "[0-9]{4}",
    "iyr": "[0-9]{4}",
    "eyr": "[0-9]{4}",
    "hgt": "[0-9]+(cm|in)",
    "hcl": "#[0-9a-f]{6}",
    "ecl": "(amb|blu|brn|gry|grn|hzl|oth)",
    "pid": "[0-9]{9}",
}


def parse_lines(lines):
    c = []
    passport = ""
    for line in lines:
        if line == "":
            c.append(passport)
            passport = ""
            continue
        passport += line + " "
    return c


def passport_to_dict(passport):
    fields = passport.split(" ")
    passport_dict = {}
    for field in fields:
        if field == "":
            continue
        key, value = field.split(":")
        if key == "cid":
            continue
        passport_dict[key] = value
    return passport_dict


def is_valid_passport(passport_dict):
    passport_dict = passport_dict
    for key, value in passport_dict.items():
        match = re.match(REGEX[key], value)
        if match is None:
            return False

        if key == "byr":
            year = int(match.string)
            if 1920 > year or year > 2002:
                return False
        elif key == "iyr":
            year = int(match.string)
            if 2010 > year or year > 2020:
                return False
        elif key == "eyr":
            year = int(match.string)
            if 2020 > year or year > 2030:
                return False
        elif key == "hgt":
            string = match.string
            value = int(string[:-2])
            unit = string[-2:]
            if unit == "cm":
                if 150 > value or value > 193:
                    return False
            elif unit == "in":
                if 59 > value or value > 76:
                    return False
            else:
                return False
        elif key == "hcl" or key == "ecl" or key == "pid":
            continue
        else:
            return False

    return True


def count(content, condition):
    count = 0
    for passport in content:
        passport_dict = passport_to_dict(passport)
        if condition(passport_dict):
            count += 1
    print("# valid passports: {}".format(count))


def condition_part1(x):
    return len(x.keys()) == 7


def part1(content):
    count(content, condition_part1)


def condition_part2(x):
    return len(x.keys()) == 7 and is_valid_passport(x)


def part2(content):
    count(content, condition_part2)


if __name__ == "__main__":
    content = parse_lines(misc.read_content())
    part1(content)
    part2(content)
