import unittest

from first import read_measurements, count_increases
from second import get_three_measurement_sums


class TestDayOne(unittest.TestCase):

    def test_reads_from_file_into_list(self):
        self.assertListEqual(
                            read_measurements('test_input.txt'),
                            [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        )

    def test_count_increases_returns_count(self):
        measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(count_increases(measurements), 7)

    def test_get_three_measurements_sums_returns_list_of_sums(self):
        measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(get_three_measurement_sums(measurements), 
                        [607, 618, 618, 617, 647, 716, 769, 792])


if __name__ == '__main__':
    unittest.main()
