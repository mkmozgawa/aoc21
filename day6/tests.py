import unittest

from first import read_file, add_fish_naive
from second import create_fish_map, add_fish_with_power

class TestDaySix(unittest.TestCase):

    def test_read_file_returns_list_of_numbers(self):
        nums = read_file('test_input.txt')
        self.assertListEqual(nums, [3, 4, 3, 1, 2])

    def test_add_fish_naively_works_for_smaller_numbers_of_days(self):
        fish = [3, 4, 3, 1, 2]
        days = 80
        for _ in range(days):
            fish = add_fish_naive(fish)
        self.assertEqual(len(fish), 5934)

    def test_create_fish_map_turns_fish_list_into_fish_map(self):
        fish = [3, 4, 3, 1, 2]
        fish_map = create_fish_map(fish)
        self.assertDictEqual(fish_map, {1: 1, 2: 1, 3: 2, 4: 1})
    
    def test_add_fish_with_power_works_for_smaller_numbers(self):
        fish = {1: 1, 2: 1, 3: 2, 4: 1}
        days = 80
        fish = add_fish_with_power(fish, days)
        self.assertEqual(sum(fish.values()), 5934)

    def test_add_fish_with_power_works_for_bigger_numbers(self):
        fish = {1: 1, 2: 1, 3: 2, 4: 1}
        days = 256
        fish = add_fish_with_power(fish, days)
        self.assertEqual(sum(fish.values()), 26984457539)