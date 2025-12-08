import heapq
from collections import defaultdict

points = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        point_str = line.strip()
        coordinates = point_str.split(',')
        points.append((int(coordinates[0]), int(coordinates[1]), int(coordinates[2])))

n = len(points)

# make-set
parent = [i for i in range(n)]
rank = [0] * n

# find
def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]

# union
def union(i, j):
    par_i = find(i)
    par_j = find(j)

    if par_i == par_j:
        return False
    
    if rank[par_i] > rank[par_j]:
        parent[par_j] = par_i
    elif rank[par_i] < rank[par_j]:
        parent[par_i] = par_j
    else:
        parent[par_j] = par_i
        rank[par_i] += 1

    return True

def distance3D_squared(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2

priority_queue = []

for i in range(n):
    for j in range(i + 1, n):
        distance = distance3D_squared(points[i], points[j])
        heapq.heappush(priority_queue, (distance, (i, j)))

connections_cnt = 1000

for i in range(connections_cnt):
    shortest_distance, (i, j) = heapq.heappop(priority_queue)
    union(i, j)

parent_freq = defaultdict(int)
res = 1

for i in range(n):
    parent_freq[find(i)] += 1

take_freqs_cnt = 3
max_freqs = sorted(parent_freq.values(), reverse = True)[:take_freqs_cnt]

for freq in max_freqs:
    res *= freq

print(res)