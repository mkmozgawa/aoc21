import unittest

from first import find_most_common_bit, inverse, return_nth_elements, binary_string_to_decimal
from second import get_matching_lines, find_least_common_bit

class TestDayThree(unittest.TestCase):
    
    def test_find_most_common_bit(self):
        bits = [0,1,1,1,0,0,1,1,1,0,0]
        self.assertEqual(find_most_common_bit(bits), 1)

    def test_find_most_common_bit_for_equal_number_of_bits(self):
        bits = [0,1,0,1,0,1,0,1]
        self.assertEqual(find_most_common_bit(bits), 1)
        self.assertEqual(find_most_common_bit(bits, preferred=1), 1)
        self.assertEqual(find_most_common_bit(bits, preferred=0), 0)

    def test_finds_least_common_bit(self):
        bits = [0,1,1,1,0,0,1,1,1,0,0]
        self.assertEqual(find_least_common_bit(bits), 0)

    def test_find_least_common_bit_for_equal_number_of_bits(self):
        bits = [0,1,0,1,0,1,0,1]
        self.assertEqual(find_least_common_bit(bits), 0)
        self.assertEqual(find_least_common_bit(bits, preferred=0), 0)
        self.assertEqual(find_least_common_bit(bits, preferred=1), 1)

    def test_returns_nth_elements_from_list_of_lists(self):
        bits = [[0,0,1,0,0], [1,1,1,1,0], [1,0,1,1,0]]
        self.assertListEqual(return_nth_elements(bits, 0), [0,1,1])
        self.assertListEqual(return_nth_elements(bits, 1), [0,1,0])
        self.assertListEqual(return_nth_elements(bits, 2), [1,1,1])
        self.assertListEqual(return_nth_elements(bits, 3), [0,1,1])
        self.assertListEqual(return_nth_elements(bits, 4), [0,0,0])

    def test_binary_string_to_decimal_returns_correct_number(self):
        self.assertEqual(binary_string_to_decimal('10110'), 22)
        self.assertEqual(binary_string_to_decimal('01001'), 9)

    def test_get_matching_lines(self):
        lines = [[0,0,1,0,0], [1,1,1,1,0], [1,0,1,1,0]]
        self.assertListEqual(get_matching_lines(lines, 0, 1), [[1,1,1,1,0], [1,0,1,1,0]])
        self.assertListEqual(get_matching_lines(lines, 4, 0), [[0,0,1,0,0], [1,1,1,1,0], [1,0,1,1,0]])
