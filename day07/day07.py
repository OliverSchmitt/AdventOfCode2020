import sys
sys.path.insert(0, "..")

import misc


def parse_lines(lines):
    rules = {}
    for line in lines:
        outer_bag, inner_bags = line[:-1].split(" contain ")
        outer_color = outer_bag.replace(" bags", "")
        inner_bags_list = inner_bags.split(", ")
        inner_bags_dict = {}
        for inner_bags_string in inner_bags_list:
            inner_bags_words = inner_bags_string.split(" ")
            amount = inner_bags_words[0]
            inner_color = inner_bags_words[1] + " " + inner_bags_words[2]
            if inner_bags_string == "no other bags":
                inner_bags_dict[inner_bags_string] = None
            else:
                inner_bags_dict[inner_color] = amount
        rules[outer_color] = inner_bags_dict
    return rules


def part1(inverted_rules):
    keys = inverted_rules.keys()
    colors = set()
    possible_colors = ["shiny gold"]
    while len(possible_colors) > 0:
        possible_color = possible_colors[0]
        possible_colors = [c for c in possible_colors if c != possible_color]
        if possible_color not in keys:
            continue
        for outer_color in inverted_rules[possible_color]:
            possible_colors.append(outer_color)
            colors.add(outer_color)
    for color in colors:
        print(color)
    print("Number of colors: {}".format(len(colors)))


def part2(rules):
    num_bags = 0
    needed_bags = ["shiny gold"]
    while len(needed_bags) > 0:
        needed_bag = needed_bags[0]
        needed_bags.remove(needed_bag)
        for bag, amount in rules[needed_bag].items():
            if amount is None:
                continue
            amount = int(amount)
            for i in range(amount):
                needed_bags.append(bag)
            num_bags += amount
    print("Number of required bags: {}".format(num_bags))


def invert_rules(rules):
    inverted_rules = {}
    for outer_color, inner_bags in rules.items():
        for inner_color, amount in inner_bags.items():
            try:
                inverted_rules[inner_color] += [outer_color]
            except KeyError:
                inverted_rules[inner_color] = [outer_color]
    return inverted_rules


if __name__ == "__main__":
    rules = parse_lines(misc.read_content())
    inverted_rules = invert_rules(rules)
    part1(inverted_rules)
    part2(rules)
