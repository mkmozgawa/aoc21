from first import read_file


def sum_of_arithmetic_sequence(a1,an):
    n = an - a1
    return int((1+n)/2*n)


def count_total_distance_to(lst,el):
    count = 0
    for num in lst:
        count += sum_of_arithmetic_sequence(min([num,el]), max([num,el]))
    return count


def find_shortest_route(lst):
    best_distance = 1000000000000 # big number to start
    for num in range(0, max(lst)):
        if (c:=count_total_distance_to(lst, num)) < best_distance:
            best_distance = c
    return best_distance
    

if __name__ == '__main__':
    positions = read_file('input.txt')
    print(find_shortest_route(positions)) # 88612508