from collections import namedtuple

Line = namedtuple('Line', 'start_x start_y end_x end_y')

def read_file(filename):
    with open(filename, 'r') as f:
        return [line for line in f.readlines()]

def multiple_lines_of_text_to_coordinates(text_lines):
    return [line_of_text_to_coordinates(line) for line in text_lines]

def line_of_text_to_coordinates(text_line):
    start, end = [x.split(',') for x in text_line.rstrip().split(' -> ')]
    return Line(start_x=min([int(start[0]), int(end[0])]), 
                start_y=min([int(start[1]), int(end[1])]), 
                end_x=max([int(start[0]), int(end[0])]), 
                end_y=max([int(start[1]), int(end[1])])
            )

def create_empty_diagram(n):
    return [[0 for el in range(0,n)] for row in range(0,n)]

def pretty_print_diagram(diagram):
    for line in diagram:
        print(f'{line}')

def apply_line_to_diagram(diagram, line):
    if line.start_y != line.end_y and line.start_x != line.end_x:
        return diagram
    changed_diagram = diagram
    for row in range(line.start_y, line.end_y+1):
        for el in range(line.start_x, line.end_x+1):
            changed_diagram[row][el] += 1
    return changed_diagram

def count_intersections(diagram):
    count = 0
    for row in diagram:
        for el in row:
            if el > 1:
                count += 1
    return count
    

if __name__ == '__main__':
    text = read_file('input.txt')
    lines = multiple_lines_of_text_to_coordinates(text)
    diagram = create_empty_diagram(1000)
    for line in lines:
        diagram = apply_line_to_diagram(diagram, line)
    print(count_intersections(diagram)) # 8350
