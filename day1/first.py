def read_measurements(filename):
    with open(filename, 'r') as f:
        return [int(line.rstrip()) for line in f]

def count_increases(lst):
    return sum([1 if first < second else 0 for first, second in zip(lst, lst[1:])])


if __name__ == '__main__':
    measurements = read_measurements('input.txt')
    count = count_increases(measurements)
    print(f'No. of increases: {count}') # 1583
