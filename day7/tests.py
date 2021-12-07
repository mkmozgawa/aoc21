import unittest

from first import read_file, count_total_distance_to
from second import sum_of_arithmetic_sequence


class TestDaySeven(unittest.TestCase):

    def test_read_file_returns_a_list(self):
        self.assertListEqual(read_file('test_input.txt'), [16,1,2,0,4,2,7,1,2,14])
    
    def test_count_total_distance_to_returns_distance_of_all_other_elements_from_one_element(self):
        self.assertEqual(count_total_distance_to([16,2], 4), 14)

    def test_sum_of_arithmetic_sequence_returns_a_sum(self):
        self.assertEqual(sum_of_arithmetic_sequence(5, 16), 66)
        self.assertEqual(sum_of_arithmetic_sequence(1,5), 10)
        self.assertEqual(sum_of_arithmetic_sequence(2,5), 6)
        self.assertEqual(sum_of_arithmetic_sequence(0,5), 15)
    