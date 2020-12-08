import sys
sys.path.insert(0, "..")

import misc


def parse_lines(lines):
    c = []
    for line in lines:
        c.append(line.split(" "))
    return c


def traverse_program(instructions):
    counter = 0
    executed = [False] * len(instructions)
    instruction_pointer = 0
    while True:
        if executed[instruction_pointer]:
            successful = False
            break
        executed[instruction_pointer] = True

        instruction, argument = instructions[instruction_pointer]
        if instruction == "nop":
            instruction_pointer += 1
        elif instruction == "acc":
            counter += int(argument)
            instruction_pointer += 1
        elif instruction == "jmp":
            instruction_pointer += int(argument)
        else:
            print("Unknown instruction '{}'".format(instruction))

        if instruction_pointer == len(instructions):
            successful = True
            break
    return counter, successful


def part1(content):
    counter, _ = traverse_program(content)
    print("Counter before executing an instruction twice: {}".format(counter))


def part2(content):
    for index, (instruction, argument) in enumerate(content):
        instructions = content.copy()
        if instruction == "nop":
            instructions[index] = ["jmp", argument]
        elif instruction == "jmp":
            instructions[index] = ["nop", argument]
        elif instruction == "acc":
            continue
        else:
            print("Unknown instruction '{}'".format(instruction))

        counter, successful = traverse_program(instructions)

        if successful:
            print("Counter after successful execution: {}".format(counter))
            break
    else:
        print("No successful execution")


if __name__ == "__main__":
    content = parse_lines(misc.read_content())
    part1(content)
    part2(content)
