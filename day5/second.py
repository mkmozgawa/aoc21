from first import read_file, create_empty_diagram, is_horizontal_or_vertical, apply_line_to_diagram, count_intersections, Line, multiple_lines_of_text_to_coordinates

def is_diagonal(line):
    return (
        abs(line.start_x - line.end_x) == abs(line.start_y - line.end_y)
        and not(is_horizontal_or_vertical(line))
    )

def apply_line_to_diagram_diagonally(diagram, line):

    changed_diagram = diagram

    if line.start_x < line.end_x and line.start_y > line.end_y:
        point = [line.end_x, line.end_y]
        for row in range(line.end_y, line.start_y+1):
            for el in range(line.start_x, line.end_x+1):
                if row == point[1] and el == point[0]:
                    changed_diagram[row][el] += 1
                    point[1] += 1
                    point[0] -= 1

    if line.start_x > line.end_x and line.start_y < line.end_y:
        point = [line.start_x, line.start_y]
        for row in range(line.start_y, line.end_y+1):
            for el in range(line.end_x, line.start_x+1):
                if row == point[1] and el == point[0]:
                    changed_diagram[row][el] += 1
                    point[1] += 1
                    point[0] -= 1

    else:
        if line.start_x > line.end_x:
            line = Line(line.end_x, line.end_y, line.start_x, line.start_y)
        point = [line.start_x, line.start_y]
        for row in range(line.start_y, line.end_y+1):
            for el in range(line.start_x, line.end_x+1):
                if row == point[1] and el == point[0]:
                    changed_diagram[row][el] += 1
                    point[1] += 1
                    point[0] += 1
    return changed_diagram

if __name__ == '__main__':
    text = read_file('input.txt')
    lines = multiple_lines_of_text_to_coordinates(text)
    diagram = create_empty_diagram(1000)
    for i, line in enumerate(lines):
        if is_horizontal_or_vertical(line):
            diagram = apply_line_to_diagram(diagram, line)
        if is_diagonal(line):
            diagram = apply_line_to_diagram_diagonally(diagram, line)
    print(count_intersections(diagram)) # 19374
