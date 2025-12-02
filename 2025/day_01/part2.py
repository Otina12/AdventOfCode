file = open(r"2025\day_01\input.txt", "r")
input = [line.strip() for line in file.readlines()]

cur_dial = 50
res = 0

for num_str in input:
    dir = num_str[0]
    rotate_by = int(num_str[1:])

    res += rotate_by // 100
    rotate_by %= 100

    if dir == 'L':
        if cur_dial != 0 and cur_dial < rotate_by:
            res += 1
        cur_dial = (cur_dial - rotate_by) % 100
    else:
        if cur_dial != 0 and cur_dial > 100 - rotate_by:
            res += 1
        cur_dial = (cur_dial + rotate_by) % 100

    if cur_dial == 0:
        res += 1

print(res)