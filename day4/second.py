from first import process_file, create_empty_tables, calculate_empty_table_position


def return_last_winning(bingo_tables, drawn_numbers):
    empty_tables = create_empty_tables(len(bingo_tables))
    bingo_tables_sums = [sum(t) for t in bingo_tables]
    board_ids = list(range(len(bingo_tables)))
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
                        if len(board_ids) == 1 and board_ids[0] == et_index:
                            return((bingo_tables_sums[et_index], num))
                        else:
                            if et_index in board_ids:
                                board_ids.remove(et_index)
                        continue

if __name__ == '__main__':
    drawn_numbers, bingo_tables = process_file('input.txt')
    sum_of_unmarked, winning_number = return_last_winning(bingo_tables, drawn_numbers)
    print(sum_of_unmarked * winning_number) # 15561
    