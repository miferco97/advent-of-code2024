import os, sys




def read_input(input_file):
    col1 , col2 = [], []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            col1.append(int(line.split()[0]))
            col2.append(int(line.split()[1]))

    sorted_col1 = sorted(col1)
    sorted_col2 = sorted(col2)
    return sorted_col1, sorted_col2


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print("File not found")
        sys.exit(1)
    input_data = read_input(input_file)
    col1, col2 = input_data
    total_dist = 0
    for i in range(len(col1)):
        dist = abs(int(col1[i]) - int(col2[i]))
        total_dist += dist
    print(f'Total distance: {total_dist}')
    similarty_total = 0
    for val in col1:
        count = col2.count(val)
        similarty_total += val * count
    print(f'Total similarity: {similarty_total}')
    



