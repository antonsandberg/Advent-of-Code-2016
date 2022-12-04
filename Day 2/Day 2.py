
with open('input.txt') as f:
    data = f.read().split()

phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

curr_index = [1, 1]
number = []
for row in data:
    sequence = [x for x in row]
    for x in sequence:
        if x == 'U':
            d_pos = (-1, 0)
        elif x == 'D':
            d_pos = (1, 0)
        elif x == 'R':
            d_pos = (0, 1)
        else:
            d_pos = (0, -1)
        test_curr_index = [curr_index[0]+d_pos[0], curr_index[1]+d_pos[1]]

        if not ((0 <= test_curr_index[0] < 3) and (0 <= test_curr_index[1] < 3)):

            continue
        for i in range(2):
            curr_index[i] += d_pos[i]
    number.append(phone[curr_index[0]][curr_index[1]])
print(number)