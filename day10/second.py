from first import read_file, remove_complete_parenthesis, find_first_close


def reverse_pairs(string):
    reverse_string = ''
    chars_open = ['(', '[', '{', '<']
    chars_close = [')', ']', '}', '>']
    for char in string:
        if char in chars_open:
            reverse_string += chars_close[chars_open.index(char)]
        if char in chars_close:
            reverse_string += chars_open[chars_close.index(char)]
    return reverse_string[::-1]


def is_corrupt(string):
    return (cor:=find_first_close(string)) is not None


def count_scores(string):
    count = 0
    values = {')': 1, ']': 2, '}': 3, '>': 4}
    for char in string:
        count *= 5
        count += values[char]
    return count


if __name__ == '__main__':
    lines = read_file('input.txt')
    scores = []
    for line in lines:
        short = remove_complete_parenthesis(line)
        if is_corrupt(short):
            continue
        completion = reverse_pairs(short)
        scores.append(count_scores(completion))
    scores = sorted(scores, reverse=True)
    print(scores[len(scores)//2]) # 4361305341

