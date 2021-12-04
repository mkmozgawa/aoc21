import unittest

from first import process_file, create_empty_tables, calculate_empty_table_position, return_first_winning
from second import return_last_winning

NUMBERS = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
TABLES = [
         [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19], 
         [3, 15, 0, 2, 22, 9, 18, 13, 17, 5, 19, 8, 7, 25, 23, 20, 11, 10, 24, 4, 14, 21, 16, 12, 6], 
         [14, 21, 17, 24, 4, 10, 16, 15, 9, 19, 18, 8, 23, 26, 20, 22, 11, 13, 6, 5, 2, 0, 12, 3, 7]
         ]

class TestDayFour(unittest.TestCase):

    def test_file_processing(self):
        numbers, tables = process_file('test_input.txt')
        self.assertListEqual(numbers, NUMBERS)
        self.assertListEqual(tables, TABLES)
        for i, table in enumerate(TABLES):
            self.assertListEqual(tables[i], table)

    def test_empty_tables_generator(self):
        tables = create_empty_tables(3)
        self.assertEqual(len(tables), 3)
        self.assertListEqual(tables[0], [0,0,0,0,0,0,0,0,0,0])

    def test_calculate_empty_table_position(self):
        self.assertEqual(calculate_empty_table_position(7), (1,2))
        self.assertEqual(calculate_empty_table_position(23), (4,3))
        self.assertEqual(calculate_empty_table_position(11), (2,1))

    def test_return_first_winning(self):
        sum_of_unmarked, winning_number = return_first_winning(TABLES, NUMBERS)
        self.assertEqual(sum_of_unmarked, 188)
        self.assertEqual(winning_number, 24)

    def test_return_last_winning(self):
        sum_of_unmarked, winning_number = return_last_winning(TABLES, NUMBERS)
        self.assertEqual(sum_of_unmarked, 148)
        self.assertEqual(winning_number, 13)
