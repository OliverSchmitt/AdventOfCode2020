import sys
sys.path.insert(0, "..")

import misc


def parse_lines(lines, split):
    c = []
    answers = ""
    for line in lines:
        if line == "":
            if len(split) != 0:
                c.append(answers[:-len(split)])
            else:
                c.append(answers)
            answers = ""
            continue
        answers += line + split
    if len(split) != 0:
        c.append(answers[:-len(split)])
    else:
        c.append(answers)
    return c


def part1(content):
    yes_answer_count = 0
    for answers in content:
        yes_answers = {}
        for question in answers:
            yes_answers[question] = 1
        yes_answer_count += len(yes_answers)
    print("Sum of yes answers: {}".format(yes_answer_count))


def part2(content):
    answer_count = 0
    for answers_group in content:
        answers_list = answers_group.split(" ")
        answers = answers_list[0]
        answer_list = [question for question in answers]
        for answers in answers_list[1:]:
            new_answer_list = []
            for question in answers:
                if question in answer_list:
                    new_answer_list.append(question)
            answer_list = new_answer_list
        answer_count += len(answer_list)
    print("Sum of yes answers: {}".format(answer_count))


if __name__ == "__main__":
    content = misc.read_content()
    part1(parse_lines(content, ""))
    part2(parse_lines(content, " "))
