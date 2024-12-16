import heapq

file = open(r"2024\day_16\input.txt", "r")
map = [list(line.strip()) for line in file.read().split('\n')]

rows, cols = len(map), len(map[0])

# 0: up, 1: right, 2: down, 3: left
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cur_dir = 1

r, c = 0, 0

for i in range(rows):
    for j in range(cols):
        if map[i][j] == 'S':
            r, c = i, j

def dijkstra(start_r, start_c):
    priority_queue = [(0, (start_r, start_c, 1))]
    visited = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]

    while priority_queue:
        cost, (i, j, cur_dir) = heapq.heappop(priority_queue)

        if map[i][j] == '#' or visited[i][j][cur_dir]:
            continue

        visited[i][j][cur_dir] = True

        if map[i][j] == 'E':
            return cost

        heapq.heappush(priority_queue, (cost + 1, (i + dirs[cur_dir][0], j + dirs[cur_dir][1], cur_dir)))
        heapq.heappush(priority_queue, (cost + 1000, (i, j, (cur_dir - 1) % 4)))
        heapq.heappush(priority_queue, (cost + 1000, (i, j, (cur_dir + 1) % 4)))
        
    return -1

res = dijkstra(r, c)
print(res)