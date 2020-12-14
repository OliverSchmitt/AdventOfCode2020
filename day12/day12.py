import sys
sys.path.insert(0, "..")

import misc


rotations = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N"
}


def get_key_by_value(dict, value):
    for key, v in dict.items():
        if v == value:
            return key


def parse_lines(lines):
    c = []
    for line in lines:
        c.append([line[0], int(line[1:])])
    return c


def rotate(action, value, direction):
    n = value // 90
    for _ in range(n):
        if action == "R":
            direction = rotations[direction]
        elif action == "L":
            direction = get_key_by_value(rotations, direction)
        else:
            print("Unknown action {} for rotation".format(action))
    return direction


def apply_action(action, value, north_south, east_west, direction):
    if action == "N":
        north_south += value
    elif action == "S":
        north_south -= value
    elif action == "E":
        east_west += value
    elif action == "W":
        east_west -= value
    elif action == "F":
        north_south, east_west, direction = apply_action(direction, value, north_south, east_west, direction)
    elif action == "R" or action == "L":
        direction = rotate(action, value, direction)
    else:
        print("Unknown action {}".format(action))

    return north_south, east_west, direction


def part1(content):
    north_south = 0
    east_west = 0
    direction = "E"
    for action, value in content:
        north_south, east_west, direction = apply_action(action, value, north_south, east_west, direction)

    print("North / south: {}\nEast / west: {}\nManhatten distance: {}".format(
        north_south,
        east_west,
        abs(north_south) + abs(east_west)
    ))


def rotate_right_2(waypoint_north_south, waypoint_east_west):
    return -waypoint_east_west, waypoint_north_south


def rotate_left_2(waypoint_north_south, waypoint_east_west):
    return waypoint_east_west, -waypoint_north_south


def rotate_2(waypoint_north_south, waypoint_east_west, action, value):
    n = value // 90
    for _ in range(n):
        if action == "R":
            waypoint_north_south, waypoint_east_west = rotate_right_2(waypoint_north_south, waypoint_east_west)
        elif action == "L":
            waypoint_north_south, waypoint_east_west = rotate_left_2(waypoint_north_south, waypoint_east_west)

    return waypoint_north_south, waypoint_east_west


def apply_action_2(north_south, east_west, waypoint_north_south, waypoint_east_west, action, value):
    if action == "N":
        waypoint_north_south += value
    elif action == "S":
        waypoint_north_south -= value
    elif action == "E":
        waypoint_east_west += value
    elif action == "W":
        waypoint_east_west -= value
    elif action == "F":
        north_south, east_west, _ = apply_action(
            "N",
            waypoint_north_south * value,
            north_south,
            east_west,
            ""
        )
        north_south, east_west, _ = apply_action(
            "E",
            waypoint_east_west * value,
            north_south,
            east_west,
            ""
        )
    elif action == "R" or action == "L":
        waypoint_north_south, waypoint_east_west = rotate_2(waypoint_north_south, waypoint_east_west, action, value)

    return north_south, east_west, waypoint_north_south, waypoint_east_west


def part2(content):
    north_south = 0
    east_west = 0
    waypoint_north_south = 1
    waypoint_east_west = 10
    for action, value in content:
        if action == "L":
            north_south = north_south
        north_south, east_west, waypoint_north_south, waypoint_east_west = apply_action_2(
            north_south, east_west, waypoint_north_south, waypoint_east_west, action, value
        )

    print("North / south: {}\nEast / west: {}\nManhatten distance: {}".format(
        north_south,
        east_west,
        abs(north_south) + abs(east_west)
    ))


if __name__ == "__main__":
    content = parse_lines(misc.read_content())
    part1(content)
    part2(content)
