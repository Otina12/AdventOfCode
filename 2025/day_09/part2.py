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
edges = []
sizes = []

for i in range(n):
    edges.append(sorted((points[i], points[i-1])))

    for j in range(i + 1, n):
        c1, c2 = sorted((points[i], points[j]))
        sizes.append((get_size(c1[0], c1[1], c2[0], c2[1]), c1, c2))
 
edges.sort(reverse = True, key = lambda e: get_size(e[0][0], e[0][1], e[1][0], e[1][1]))
sizes.sort(reverse = True)
res = 0

for size, (x1, y1), (x2, y2) in sizes:
    y1, y2 = sorted((y1, y2))
    if not any((x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2) for (x3, y3), (x4, y4) in edges):
        res = size
        break

print(res)