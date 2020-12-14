import sys
sys.path.insert(0, "..")

import misc


def part1(ratings):
    chains = []

    configurations = [[ratings, max(ratings) + 3, 0, 0, []]]

    while len(configurations) > 0:
        remaining_ratings, max_rating, num_1_differences, num_3_differences, chain = configurations[0]
        configurations = configurations[1:]

        # if len(remaining_ratings) == 0 and max_rating <= 3:
        if max_rating <= 3:
            if len(remaining_ratings) == 0:
                num_3_differences = num_3_differences
            if max_rating == 1:
                num_1_differences += 1
            elif max_rating == 3:
                num_3_differences += 1
            chains.append([len(remaining_ratings) == 0, num_1_differences, num_3_differences, chain])
            # continue
            # break

        possible_ratings = []
        for rating in remaining_ratings:
            if rating + 1 <= max_rating <= rating + 3:
                possible_ratings.append(rating)

        for possible_rating in possible_ratings:
            diff = max_rating - possible_rating

            new_ratings = remaining_ratings[:]
            new_ratings.remove(possible_rating)

            if diff == 1:
                configurations.insert(0, [
                    new_ratings,
                    max_rating - diff,
                    num_1_differences + 1,
                    num_3_differences,
                    chain + [possible_rating]
                ])
            elif diff == 3:
                configurations.insert(0, [
                    new_ratings,
                    max_rating - diff,
                    num_1_differences,
                    num_3_differences + 1,
                    chain + [possible_rating]
                ])
            else:
                configurations.insert(0, [
                    new_ratings,
                    max_rating - diff,
                    num_1_differences,
                    num_3_differences,
                    chain + [possible_rating]
                ])

    for all_used, num_1_differences, num_3_differences, _ in chains:
        if all_used:
            print("# 1 diff * # 3 diff = {} * {} = {}".format(num_1_differences, num_3_differences, num_1_differences * num_3_differences))

    print("# of chains: {}".format(len(chains)))


def part2(ratings):
    pass


if __name__ == "__main__":
    ratings = [int(x) for x in misc.read_content("input_test_large.txt")]
    part1(ratings)
    part2(ratings)
