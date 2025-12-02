import re

puzzle_input = []

with open(fr"2025\day_02\input.txt", "r") as file:
    text = file.readline()
    ranges = text.split(',')

    for part in ranges:
        start, end = part.split('-')
        puzzle_input.append((int(start), int(end)))

pattern = re.compile(r'^(\d+)\1+$')
res = 0

for start, end in puzzle_input:
    for x in range(start, end + 1):
        if pattern.match(str(x)):
            res += x

print(res)