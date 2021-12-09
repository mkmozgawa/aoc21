def read_file(filename):
    with open(filename, 'r') as f:
        lines = []
        for line in f.readlines():
            lines.append([int(x) for x in list(line.strip())])
    return lines


def find_low_points(list_of_points):
    # pad list with 9s, nein nein nein
    list_of_points = [[9 for x in list_of_points[0]]] + list_of_points + [[9 for x in list_of_points[0]]]
    lst = []
    for row in list_of_points:
        r = [9]
        for el in row:
            r.append(el)
        r.append(9)
        lst.append(r)

    low_points = []
    for ir in range(1, len(lst)-1):
        for ie in range(1, len(lst[ir])-1):
            top = lst[ir-1][ie]
            bottom = lst[ir+1][ie]
            left = lst[ir][ie-1]
            right = lst[ir][ie+1]
            el = lst[ir][ie]
            if el < top and el < bottom and el < left and el < right:
                low_points.append(el)
    return low_points


if __name__ == '__main__':
    input = read_file('input.txt')
    low_points = find_low_points(input)
    print(low_points)
    print(sum(low_points) + len(low_points))
