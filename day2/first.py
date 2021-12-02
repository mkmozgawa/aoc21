from collections import namedtuple


def read_file(filename):
    with open(filename, 'r') as f:
        return [(line.rstrip()) for line in f]


def read_commands(filename):
    Command = namedtuple('Command', 'name value')
    content = read_file(filename)
    return (Command._make([el[0], int(el[1])])
                for el in (x.split(' ') for x in content))

def calculate_position(commands):
    Position = namedtuple('Position', 'horizontal depth')
    horizontal = 0
    depth = 0
    for command in commands:
        if command.name == 'forward': horizontal += command.value
        if command.name == 'down': depth += command.value
        if command.name == 'up': depth -= command.value
    return Position(horizontal, depth)


if __name__ == '__main__':
    commands = read_commands('input.txt')
    position = calculate_position(commands)
    print(position.horizontal * position.depth) # 2070300
