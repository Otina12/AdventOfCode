puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [[int(num) for num in line.strip()] for line in file.readlines()]

def find_leftmost_max_digit(digits, start_idx, end_idx):
    max_num_idx, max_num = end_idx, digits[end_idx]

    for i in range(end_idx, start_idx - 1, -1):
        if digits[i] >= max_num:
            max_num = digits[i]
            max_num_idx = i
    
    return (max_num_idx, max_num)

res = 0
n = len(puzzle_input[0])

for powers in puzzle_input:
    max_power = 0
    cur_start_idx = 0
    
    for x in range(12, 0, -1):
        max_num_idx, max_num = find_leftmost_max_digit(powers, cur_start_idx, n - x)
        max_power = 10 * max_power + max_num
        cur_start_idx = max_num_idx + 1

    res += max_power

print(res)