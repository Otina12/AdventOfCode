puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [[int(num) for num in line.strip()] for line in file.readlines()]

res = 0
n = len(puzzle_input[0])

for powers in puzzle_input:
    max_ten_place = powers[0]
    max_one_place = powers[1]

    for i in range(1, n - 1):
        if powers[i] > max_ten_place:
            max_ten_place = powers[i]
            max_one_place = powers[i+1]
        elif powers[i] > max_one_place:
            max_one_place = powers[i]

    max_one_place = max(max_one_place, powers[-1])

    max_power = 10 * max_ten_place + max_one_place
    res += max_power

print(res)