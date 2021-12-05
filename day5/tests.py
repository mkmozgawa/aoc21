import unittest

from first import line_of_text_to_coordinates, read_file, Line, create_empty_diagram, apply_line_to_diagram, count_intersections

class TestDayFive(unittest.TestCase):

    def test_line_of_text_is_converted_to_points_tuple(self):
        text_line = '0,9 -> 5,9'
        coordinates = line_of_text_to_coordinates(text_line)
        self.assertEqual(coordinates.start_x, 0)
        self.assertEqual(coordinates.start_y, 9)
        self.assertEqual(coordinates.end_x, 5)
        self.assertEqual(coordinates.end_y, 9)
    
    def test_line_of_text_conversion_works_for_longer_coords_and_lower_to_higher_values(self):
        text_line = '57,611 -> 57,221'
        coordinates = line_of_text_to_coordinates(text_line)
        self.assertEqual(coordinates.start_x, 57)
        self.assertEqual(coordinates.start_y, 221)
        self.assertEqual(coordinates.end_x, 57)
        self.assertEqual(coordinates.end_y, 611)

    def test_read_file_returns_list_of_line_coordinates(self):
        lines = read_file('test_input.txt')
        self.assertListEqual(lines, ['0,9 -> 5,9\n', '8,0 -> 0,8\n', '9,4 -> 3,4\n', '2,2 -> 2,1\n', '7,0 -> 7,4\n', '6,4 -> 2,0\n', '0,9 -> 2,9\n', '3,4 -> 1,4\n', '0,0 -> 8,8\n', '5,5 -> 8,2'])

    def test_create_diagram_returns_matrix_of_zeros(self):
        diagram = create_empty_diagram(3)
        self.assertListEqual(diagram, [[0,0,0], [0,0,0], [0,0,0]])

    def test_apply_line_to_diagram_takes_empty_diagram_and_adds_to_it_based_on_line(self):
        diagram = [[0,0,0], [0,0,0], [0,0,0]]
        line = Line(start_x = 1, start_y = 0, end_x = 2, end_y = 0)
        self.assertListEqual(apply_line_to_diagram(diagram, line),
                             [[0,1,1], [0,0,0], [0,0,0]])

    def test_apply_line_to_diagram_takes_filled_diagram_and_adds_to_it_based_on_line(self):
        diagram = [[0,1,1], [0,0,0], [0,0,0]]
        line = Line(start_x = 0, start_y = 0, end_x = 1, end_y = 0)
        self.assertListEqual(apply_line_to_diagram(diagram, line),
                             [[1,2,1], [0,0,0], [0,0,0]])

    def test_apply_line_to_diagram_works_if_the_line_is_a_point(self):
        diagram = [[0,0,0], [0,0,0], [0,0,0]]
        line = Line(start_x = 0, start_y = 0, end_x = 0, end_y = 0)
        self.assertListEqual(apply_line_to_diagram(diagram, line),
                             [[1,0,0], [0,0,0], [0,0,0]])

    def test_apply_line_to_diagram_returns_old_diagram_if_line_is_not_horizontal_or_vertical(self):
        diagram = [[0,1,1], [0,0,0], [0,0,0]]
        line = Line(start_x = 0, start_y = 0, end_x = 1, end_y = 2)
        self.assertListEqual(apply_line_to_diagram(diagram, line),
                             [[0,1,1], [0,0,0], [0,0,0]])

    def test_it_finds_intersections_of_two_or_more_lines(self):
        diagram = [[1,2,1],[0,2,0],[0,0,0]]
        self.assertEqual(count_intersections(diagram), 2)
