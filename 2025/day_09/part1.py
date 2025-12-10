points = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        point_str = line.strip()
        coordinates = point_str.split(',')
        points.append((int(coordinates[0]), int(coordinates[1])))

def get_size(x1, y1, x2, y2):
    x = abs(x1 - x2) + 1
    y = abs(y1 - y2) + 1
    return x * y

n = len(points)
res = 0

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        res = max(res, get_size(x1, y1, x2, y2))

print(res)