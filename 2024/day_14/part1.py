import re

file = open(r"2024\day_14\input.txt", "r")
input = [line.strip() for line in file.readlines()]

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
robots = []

for line in input:
    x, y, dx, dy = map(int, re.search(pattern, line).groups())
    robots.append((x, y, dx, dy))

rows, cols = 103, 101

quadrants = [0, 0, 0, 0]

for robot in robots:
    x, y, dx, dy = robot
    for _ in range(100):
        x = (x + dx) % cols
        y = (y + dy) % rows
    
    if y < rows // 2:
        if x < cols // 2:
            quadrants[0] += 1
        elif x > cols // 2:
            quadrants[1] += 1
    elif y > rows // 2:
        if x < cols // 2:
            quadrants[2] += 1
        elif x > cols // 2:
            quadrants[3] += 1

res = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(res)