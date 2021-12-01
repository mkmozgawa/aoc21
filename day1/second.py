from first import read_measurements, count_increases


def get_three_measurement_sums(lst):
    return [sum(three) for three in list(zip(lst, lst[1:], lst[2:]))]

if __name__ == '__main__':
    measurements = read_measurements('input.txt')
    sums = get_three_measurement_sums(measurements)
    count = count_increases(sums)
    print(f'No. of increases in sums of three: {count}') # 1627
