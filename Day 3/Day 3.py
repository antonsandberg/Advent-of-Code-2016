from itertools import permutations
import numpy as np
import time
from copy import deepcopy

def collect_data(filename):
    with open(filename) as f:
        data = [[int(y) for y in x.strip().split()] for x in f.readlines()]
    return data


def main():
    FILENAME = 'Day 3/input.txt'
    data = np.array(collect_data(FILENAME))
    data_shape = data.shape
    data_2 = np.copy(data)
    data_2 = data_2.flatten(order="F")
    data_2 = data_2.reshape(data_shape)

    part_1 = 0
    part_2 = 0
    
    # Part 1
    for values in data:
        bools = []
        for perms in permutations(values):
            bools.append((perms[0] + perms[1]) > perms[2])
        if all(bools):
            part_1 += 1

    # Part 2
    for values in data_2:
        bools = []
        for perms in permutations(values):
            bools.append((perms[0] + perms[1]) > perms[2])
        if all(bools):
            part_2 += 1

    print(f'Day 3 part 1: {part_1}')
    print(f'Day 3 part 2: {part_2}')

if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f'Time taken: {t2-t1:-6f}s')

