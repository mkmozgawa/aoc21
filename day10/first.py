def read_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def remove_complete_parenthesis(string):
    pairs = ['[]', '()', '{}', '<>']
    # print(string)
    new_string = string
    for pair in pairs:
        if pair in string:
            new_string = string.replace(pair, '')
    if string == new_string:
        return new_string
    else:
        return remove_complete_parenthesis(new_string)  


def find_first_close(string):
    for char in list(string):
        if char in [')', ']', '}', '>']:
            return char
    return None


def count_points(corruptions):
    count = 0
    for cor in corruptions:
        if cor == ')': count += 3
        if cor == ']': count += 57
        if cor == '}': count += 1197
        if cor == '>': count += 25137
    return count


if __name__ == '__main__':
    lines = read_file('test_input.txt')
    corruptions = []
    for line in lines:
        short = remove_complete_parenthesis(line)
        if (cor:=find_first_close(short)) is not None:
            corruptions.append(cor)
    print(count_points(corruptions)) # 318081

