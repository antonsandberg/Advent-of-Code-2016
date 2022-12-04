from itertools import permutations
import numpy as np

with open('input.txt') as f:
    data = [[int(y) for y in x.strip().split()] for x in f.readlines()]

data = np.array(data)
data_shape = data.shape
data = data.flatten(order="F")
data = data.reshape(data_shape)

good_values = 0
for values in data:
    bools = []
    for perms in permutations(values):
        bools.append((perms[0] + perms[1]) > perms[2])
    if all(bools):
        good_values += 1

print(good_values)

