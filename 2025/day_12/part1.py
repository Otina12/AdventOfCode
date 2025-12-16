puzzle_input = []

with open("input.txt", "r") as file:
    for line in file:
        puzzle_input.append(line.strip())

fit = 0

for line in puzzle_input:
    if 'x' in line:
        dimensions, boxes = line.split(':')
        w, h = dimensions.split('x')
        area = int(w)//3 * int(h)//3

        total_boxes = sum(int(x) for x in boxes.split())
        if total_boxes <= area:
            fit += 1

print(fit)