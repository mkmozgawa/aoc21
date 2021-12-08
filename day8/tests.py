import unittest

from first import process_file


class TestDayEight(unittest.TestCase):

    def test_process_file_returns_two_lists(self):
        signal_patterns, four_digit_output_value = process_file('test_input.txt')
        self.assertListEqual(signal_patterns,
                             ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb', 
                             'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec', 
                             'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef', 
                             'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega', 
                             'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga', 
                             'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf', 
                             'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf', 
                             'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd', 
                             'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg', 
                             'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc'])
        self.assertListEqual(four_digit_output_value,
                             ['fdgacbe cefdb cefbgd gcbe', 
                             'fcgedb cgb dgebacf gc', 
                             'cg cg fdcagb cbg', 
                             'efabcd cedba gadfec cb', 
                             'gecf egdcabf bgf bfgea', 
                             'gebdcfa ecba ca fadegcb', 
                             'cefg dcbef fcge gbcadfe', 
                             'ed bcgafe cdgba cbgef', 
                             'gbdfcae bgc cg cgb', 
                             'fgae cfgab fg bagce'])

        