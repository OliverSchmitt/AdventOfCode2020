import sys
sys.path.insert(0, "..")

import misc


def traverse(content, num_rows, num_cols, incr_x, incr_y):
    tree_count = 0
    x = -incr_x
    for y in range(0, num_rows, incr_y):
        x = (x + incr_x) % num_cols
        if content[y * num_cols + x] == "#":
            tree_count += 1
    return tree_count


def part1(content, num_rows, num_cols):
    tree_count = traverse(content, num_rows, num_cols, 3, 1)
    print("Tree count: {}".format(tree_count))


def part2(content, num_rows, num_cols):
    increments = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    tree_counts = []
    for increment in increments:
        x, y = increment
        tree_count = traverse(content, num_rows, num_cols, x, y)
        print("Right: {}, down {} - {}".format(x, y, tree_count))
        tree_counts.append(tree_count)
    product = 1
    for t in tree_counts:
        product *= t
    print("Product: {} * {} * {} * {} = {}".format(tree_counts[0], tree_counts[1], tree_counts[2], tree_counts[3], product))


if __name__ == "__main__":
    lines = misc.read_content()
    num_rows = len(lines)
    num_cols = len(lines[0])
    content = "".join(lines)
    part1(content, num_rows, num_cols)
    part2(content, num_rows, num_cols)
