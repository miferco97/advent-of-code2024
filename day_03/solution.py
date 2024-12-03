import os
import sys
import re

def read_input(input_file):
    data = ''
    with open(input_file, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        data = data.join(lines)
    return data


def process_input(data):
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    regex = re.compile(regex)
    # find all matches
    matches = regex.findall(data)
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
    return sum


def filter_input(data):
    start = r"(?:^(.*?)don't\(\))"
    end = r"(?:do\(\)(.*)$)"
    mid = r"(?:do\(\)(.*?)don't\(\))+"
    regex_ = f'{start}|{mid}|{end}'

    regex_ = re.compile(regex_)
    matches = regex_.findall(data)
    value = 0
    for branch in matches:
        for capture in branch:
            value += process_input(capture)
    return value


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print("File not found")
        sys.exit(1)
    input_data = read_input(input_file)
    sum = process_input(input_data)
    print(f"Solution 1: {sum}")
    sum2 = filter_input(input_data)
    print(f"Solution 2: {sum2}")
