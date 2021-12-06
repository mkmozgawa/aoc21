from first import read_file


def create_fish_map(fish_list):
    fish_map = {}
    for fish in fish_list:
        if fish not in fish_map.keys():
            fish_map[fish] = 1
        else:
            fish_map[fish] += 1
    return fish_map


def add_fish_in_a_day(fish_map):
    new_fish_map = {i:0 for i in range(8,-1,-1)}
    for life_stage, fish_at_stage in fish_map.items():
        if life_stage > 0:
            new_fish_map[life_stage-1] = fish_at_stage
        if life_stage == 0:
            new_fish_map[8] = fish_at_stage # new fish are born
            new_fish_map[6] += fish_at_stage
    return new_fish_map


def add_fish_with_power(fish_map, days):
    for _ in range(days):
        fish_map = add_fish_in_a_day(fish_map)
    return fish_map


if __name__ == '__main__':
    fish_list = read_file('input.txt')
    fish_map = create_fish_map(fish_list)
    all_fish = add_fish_with_power(fish_map, 256)
    print(sum(all_fish.values())) # 1743335992042 0.03s user 0.01s system 85% cpu 0.045 total