def read_file(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.readline().strip().split(',')]


def count_total_distance_to(lst, el):
    count = 0
    for num in lst:
        count += abs(num-el)
    return count


def list_to_dict(lst):
    d = {}
    for el in lst:
        if el not in d.keys():
            d[el] = {'count': 1, 'total_distance_to': count_total_distance_to(lst, el)}
        else:
            d[el]['count'] += 1
    return d


if __name__ == '__main__':
    positions = read_file('input.txt')
    d = list_to_dict(positions)
    print(min([d[x]['total_distance_to'] for x in d.keys()])) # 326132