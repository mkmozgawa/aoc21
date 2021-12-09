import unittest

from first import read_file, find_low_points

class TestDayNine(unittest.TestCase):
    
    def test_reads_file_to_list_of_lists(self):
        self.assertListEqual(read_file('test_input.txt'),
                         [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], 
                         [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], 
                         [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], 
                         [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], 
                         [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])
    
    def test_returns_list_of_low_points(self):
        lst = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], 
               [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], 
               [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], 
               [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], 
               [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
        self.assertListEqual(find_low_points(lst), [1, 0, 5, 5])