import sys
sys.path.insert(0, "..")

import misc


def get_number_without_sum(content):
    number_range = 25
    for index in range(number_range, len(content)):
        number = content[index]
        has_sum = False
        for i in range(index - number_range, index):
            for j in range(i + 1, index):
                if content[i] + content[j] == number:
                    has_sum = True

        if not has_sum:
            return number



def part1(content):
    print("First number which is not a sum to 2 numbers in the last 25 numbers: {}".format(get_number_without_sum(content)))


def part2(content):
    invalid_number = get_number_without_sum(content)
    for index in range(len(content)):
        sum_of_numbers = content[index]
        inner_index = index + 1
        while sum_of_numbers < invalid_number:
            sum_of_numbers += content[inner_index]
            if sum_of_numbers == invalid_number:
                number_range = content[index:inner_index]
                print("Sum of smallest and largest number in series: {}".format(min(number_range) + max(number_range)))
            inner_index += 1


if __name__ == "__main__":
    content = [int(n) for n in misc.read_content()]
    part1(content)
    part2(content)
