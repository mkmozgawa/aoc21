def process_file(filename):
    with open(filename, 'r') as f:
        content = [line for line in f.readlines()]
        signal_patterns = [line.split('|')[0].strip() for line in content]
        four_digit_output_value = [line.split('|')[1].strip() for line in content]
        return (signal_patterns, four_digit_output_value)


if __name__ == '__main__':
    _, four_digit_output_value = process_file('input.txt')
    count = 0
    for line in four_digit_output_value:
        count += len([word for word in line.split(' ') if len(word) in (2,3,4,7)])
    print(count) # 237
