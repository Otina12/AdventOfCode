file = open(r"2025\day_01\input.txt", "r")
input = [line.strip() for line in file.readlines()]

cur_dial = 50
res = 0

for num_str in input:
    dir = num_str[0]
    rotate_by = int(num_str[1:])

    if dir == 'L':
        cur_dial = (cur_dial - rotate_by) % 100
    else:
        cur_dial = (cur_dial + rotate_by) % 100

    if cur_dial == 0:
        res += 1

print(res)