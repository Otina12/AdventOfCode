from collections import deque

file = open(r"2024\day_20\input.txt", "r")
map = [list(line.strip()) for line in file.readlines()]

rows, cols = len(map), len(map[0])
r, c = -1, -1

def in_bounds(i, j):
    return i > -1 and i < rows and j > -1 and j < cols

for i in range(rows):
    for j in range(cols):
        if map[i][j] == 'S':
            r, c = i, j
            break
    else:
        continue
    break

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
distance = [[-1] * cols for _ in range(rows)]
distance[r][c] = 0
q = deque([(r, c)])
        
while q:
    cr, cc = q.popleft()
    for dir in dirs:
        nr, nc = cr + dir[0], cc + dir[1]
        if not in_bounds(nr, nc) or map[nr][nc] == '#' or distance[nr][nc] != -1:
            continue
        distance[nr][nc] = distance[cr][cc] + 1
        q.append((nr, nc))
   
jump_dirs = [[-1, 1], [0, 2], [1, 1], [2, 0]] 
res = 0

for i in range(rows):
    for j in range(cols):
        if map[i][j] == '#':
            continue
        for dir in jump_dirs:
            ni, nj = i + dir[0], j + dir[1]
            if not in_bounds(ni, nj) or map[ni][nj] == '#':
                continue
            if abs(distance[i][j] - distance[ni][nj]) >= 102:
                res += 1
                
print(res)