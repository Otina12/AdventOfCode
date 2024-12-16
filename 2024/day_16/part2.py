from collections import defaultdict, deque

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

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c, 1, 0, set([(start_r, start_c)]))])
    visited = [[[-1] * 4 for _ in range(cols)] for _ in range(rows)]
    good_cells = defaultdict(set)

    while queue:
        i, j, cur_dir, cost, cells = queue.popleft()

        if map[i][j] == '#' or visited[i][j][cur_dir] != -1 and cost > visited[i][j][cur_dir]:
            continue

        visited[i][j][cur_dir] = cost

        if map[i][j] == 'E':
            for cell in cells:
                good_cells[cost].add(cell)
            continue
        
        queue.append((i, j, (cur_dir - 1) % 4, cost + 1000, cells))
        queue.append((i, j, (cur_dir + 1) % 4, cost + 1000, cells))
        
        new_cells = cells.copy()
        new_cells.add((i + dirs[cur_dir][0], j + dirs[cur_dir][1]))
        queue.append((i + dirs[cur_dir][0], j + dirs[cur_dir][1], cur_dir, cost + 1, new_cells))
        
    min_cost = min(good_cells.keys())
    return len(good_cells[min_cost])

res = bfs(r, c)
print(res)