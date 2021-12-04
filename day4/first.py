def process_bingo_tables(lines):
    bingo_tables = []
    table = []
    for line in lines:
        if line == '\n':
            bingo_tables.append(table)
            table = []
            continue
        table += [int(x) for x in line.strip().split(' ') if x]
    bingo_tables.append(table)
    return bingo_tables


def process_file(filename):
    with open(filename, 'r') as f:
        drawn_numbers = [int(x) for x in f.readline().rstrip().split(',')]
        f.readline() # throw away the empty line
        bingo_tables = process_bingo_tables(f.readlines())
    return (drawn_numbers, bingo_tables)


def create_empty_tables(no_of_tables):
    empty_tables = []
    for i in range(no_of_tables):
        empty_tables.append([0 for _ in range(10)])
    return empty_tables


def calculate_empty_table_position(el):
    row = el // 5
    col = el % 5
    return (row, col)


def return_first_winning(bingo_tables, drawn_numbers):
    empty_tables = create_empty_tables(len(bingo_tables))
    bingo_tables_sums = [sum(t) for t in bingo_tables]
    for num in drawn_numbers:
        for i, table in enumerate(bingo_tables):
            if num in table:
                pos = table.index(num)
                row, col = calculate_empty_table_position(pos)
                empty_tables[i][row] += 1
                empty_tables[i][col+5] += 1
                bingo_tables_sums[i] -= num
                for et_index, et in enumerate(empty_tables):
                    if 5 in et:
                        return (bingo_tables_sums[et_index], num)


if __name__ == '__main__':
    drawn_numbers, bingo_tables = process_file('input.txt')
    sum_of_unmarked, winning_number = return_first_winning(bingo_tables, drawn_numbers)
    print(sum_of_unmarked * winning_number) # 87456
                