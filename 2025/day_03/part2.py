from collections import deque

puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [[int(num) for num in line.strip()] for line in file.readlines()]

res = 0
m = len(puzzle_input[0])
k = 12

for powers in puzzle_input:
    remove_cnt = m - k
    stack = deque()

    for power in powers:
        while remove_cnt > 0 and stack and power > stack[-1]:
            stack.pop()
            remove_cnt -= 1
        stack.append(power)

    max_power = 0

    for i in range(k):
        max_power = max_power * 10 + stack[i]

    res += max_power

print(res)