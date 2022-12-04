
with open('input.txt') as f:
    data = [x.strip(',') for x in f.read().split()]

current_position = [0, 0]
direction_mods = ((-1, 0), (0, 1), (1, 0), (0, -1))
index_position = 0
visited = set()
visited.add(tuple(current_position))
for instr in data:
    direction = instr[0]
    value = int(instr[1:])
    if direction == 'R':
        index_position += 1
        index_position = index_position % 4
    else:
        index_position -= 1
        index_position = index_position % 4

    d_pos = [x*value for x in direction_mods[index_position]]
    for a in d_pos:
        for da in range(a):
            print(da)
            for i, x in enumerate(d_pos):
                current_position[i] += da
                visited.add(tuple(current_position))
    print(visited)
    if tuple(current_position) in visited:
        break



print(abs(current_position[0]) + abs(current_position[1]))
