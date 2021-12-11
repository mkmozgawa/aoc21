import unittest

from first import read_file, remove_complete_parenthesis, find_first_close, count_points


class TestDayTen(unittest.TestCase):

    def test_read_file_returns_list_of_lines(self):
        self.assertListEqual(read_file('test_input.txt'),
                            ['[({(<(())[]>[[{[]{<()<>>', 
                            '[(()[<>])]({[<{<<[]>>(', 
                            '{([(<{}[<>[]}>{[]{[(<()>', 
                            '(((({<>}<{<{<>}{[]{[]{}', 
                            '[[<[([]))<([[{}[[()]]]', 
                            '[{[{({}]{}}([{[{{{}}([]', 
                            '{<[[]]>}<{[{[{[]{()[[[]', 
                            '[<(<(<(<{}))><([]([]()', 
                            '<{([([[(<>()){}]>(<<{{', 
                            '<{([{{}}[<[[[<>{}]]]>[]]'])

    def test_remove_complete_parentheses_removes_direct_pairs(self):
        self.assertEqual(remove_complete_parenthesis('{([(<{}[<>[]}>{[]{[(<()>'),
                        '{([(<[}>{{[(')

    def test_find_first_close_finds_first_closing_parenthesis(self):
        self.assertEqual(find_first_close('([}>'), '}')

    def test_count_points_returns_count_of_points(self):
        self.assertEqual(count_points('{]])>][}'), 26508)