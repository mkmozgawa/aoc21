def split_into_ints(string):
    return [int(char) for char in string]


def read_file(filename):
    with open(filename, 'r') as f:
        return [split_into_ints(line.rstrip()) for line in f]


def return_nth_elements(lst_of_lsts_of_ints, n):
    return [lst[n] for lst in lst_of_lsts_of_ints]


def find_most_common_bit(lst_of_ints, preferred=1):
    if sum(lst_of_ints) > len(lst_of_ints) / 2:
        return 1
    if sum(lst_of_ints) == len(lst_of_ints) / 2:
        return preferred
    return 0


def inverse(most_common_bit):
    return int(not most_common_bit)


def binary_string_to_decimal(bin_str):
    return int(bin_str, 2)


if __name__ == '__main__':
    lines = read_file('input.txt')
    gamma = ''
    epsilon = ''
    for index, val in enumerate(lines[0]):
        nth_elements = return_nth_elements(lines, index)
        most_common = find_most_common_bit(nth_elements)
        gamma += str(most_common) 
        epsilon += str(inverse(most_common))
    print(binary_string_to_decimal(gamma) * binary_string_to_decimal(epsilon)) # 2583164
