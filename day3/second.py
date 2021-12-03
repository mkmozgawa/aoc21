from first import read_file, return_nth_elements, find_most_common_bit, binary_string_to_decimal

def get_matching_lines(lines_lst, nth, val):
    return [line for line in lines_lst if line[nth] == val]

def find_least_common_bit(lst_of_ints, preferred=0):
    if sum(lst_of_ints) < len(lst_of_ints) / 2:
        return 1
    if sum(lst_of_ints) == len(lst_of_ints) / 2:
        return preferred
    return 0


if __name__ == '__main__':
    lines = read_file('input.txt')
    oxygen_lines = lines
    co2_lines = lines
    for index, val in enumerate(lines[0]):
        oxygen_elements = return_nth_elements(oxygen_lines, index)
        most_common = find_most_common_bit(oxygen_elements, preferred=1)
        oxygen_lines = get_matching_lines(oxygen_lines, index, most_common)
        if len(oxygen_lines) == 1: break
    for index, val in enumerate(lines[0]):
        co2_elements = return_nth_elements(co2_lines, index)
        least_common = find_least_common_bit(co2_elements, preferred=0)
        co2_lines = get_matching_lines(co2_lines, index, least_common)
        if len(co2_lines) == 1: break
    oxygen = ''.join(map(str, oxygen_lines[0]))
    co2 = ''.join(map(str, co2_lines[0]))
    print(binary_string_to_decimal(oxygen) * binary_string_to_decimal(co2)) # 2784375
