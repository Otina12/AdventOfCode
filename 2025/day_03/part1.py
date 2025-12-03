puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [[int(num) for num in line.strip()] for line in file.readlines()]

res = 0
m = len(puzzle_input[0])

for powers in puzzle_input:
    max_ten_place = max(powers[0:m-1])
    max_ten_place_i = powers.index(max_ten_place)
    max_one_place = max(powers[max_ten_place_i+1:])

    max_power = 10 * max_ten_place + max_one_place
    res += max_power

print(res)