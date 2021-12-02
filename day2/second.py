from collections import namedtuple

from first import read_commands


def calculate_position_calibrated(commands):
    Position = namedtuple('Position', 'horizontal depth')
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        if command.name == 'down': aim += command.value
        if command.name == 'up': aim -= command.value
        if command.name == 'forward':
            horizontal += command.value
            depth += aim * command.value
    return Position(horizontal, depth)



if __name__ == '__main__':
    commands = read_commands('input.txt')
    position = calculate_position_calibrated(commands)
    print(position.horizontal * position.depth) # 2078985210
