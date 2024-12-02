import os, sys

def check_safe(values_list):
    copy_list = values_list.copy()
    sorted_list = sorted(copy_list)
    if sorted_list != copy_list and sorted_list != copy_list[::-1]:
        return False
    for i in range(len(values_list)-1):
        if abs(values_list[i] - values_list[i+1]) >3 or abs(values_list[i] - values_list[i+1]) < 1:
            return False
    return True

def brute_force_test(values_list):
    if check_safe(values_list):
        return True
    for j in range(len(values_list)):
        if check_safe(values_list[:j] + values_list[j+1:]):
            return True
    return False

def read_input(input_file):
    values = []
    with open(input_file, 'r') as f:
        for line in f:
            values.append([int(x) for x in line.split()])
    return values


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print("File not found")
        sys.exit(1)
    input_data = read_input(input_file)

    check_values = 0
    for values in input_data:
        if check_safe(values):
            check_values += 1
    print(f'[1] Number of safe values: {check_values}')

    check_values = 0
    for values in input_data:
        if brute_force_test(values):
            check_values += 1
    print(f'[2] Number of safe values: {check_values}')

