from collections import namedtuple
import unittest

from first import read_commands, calculate_position, read_file
from second import calculate_position_calibrated

class TestDayTwo(unittest.TestCase):

    def test_read_file_returns_list_of_lines(self):
        lines = read_file('test_input.txt')
        self.assertListEqual(lines, 
            ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])

    def test_read_commands_returns_named_tuples_generator(self):
        commands = read_commands('test_input.txt')
        command_1 = next(commands)
        self.assertEqual(command_1.name,'forward')
        self.assertEqual(command_1.value, 5)

    def test_calculate_position_first_returns_horizontal_and_depth(self):
        Command = namedtuple('Command', 'name value')
        commands = [Command(name='forward', value=5), Command(name='down', value=5), Command(name='forward', value=8), Command(name='up', value=3), Command(name='down', value=8), Command(name='forward', value=2)]
        position = calculate_position(commands)
        self.assertEqual(position.horizontal, 15)
        self.assertEqual(position.depth, 10)

    def test_calculate_position_second_returns_horizontal_and_depth(self):
        Command = namedtuple('Command', 'name value')
        commands = [Command(name='forward', value=5), Command(name='down', value=5), Command(name='forward', value=8), Command(name='up', value=3), Command(name='down', value=8), Command(name='forward', value=2)]
        position = calculate_position_calibrated(commands)
        self.assertEqual(position.horizontal, 15)
        self.assertEqual(position.depth, 60)
