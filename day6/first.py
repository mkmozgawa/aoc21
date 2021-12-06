def read_file(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.readline().split(',')]


def add_fish_naive(old_fish):
    new_fish = []
    for i, f in enumerate(old_fish):
        old_fish[i] -= 1
        if old_fish[i] == -1:
            old_fish[i] = 6
            new_fish.append(8)
    new_fish = old_fish + new_fish
    return new_fish 


if __name__ == '__main__':
    fish = read_file('input.txt')
    for d in range(80):
        fish = add_fish_naive(fish)
    print(len(fish)) # 389726 0.51s user 0.02s system 98% cpu 0.547 total