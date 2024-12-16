from collections import deque

file = open(r"2024\day_12\input.txt", "r")
input = [list(line.strip()) for line in file.readlines()]

rows, cols = len(input), len(input[0])
            
def in_bounds(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols

regions = []
visited = [[False] * cols for _ in range(rows)]

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
corner_dirs = [[-0.5, -0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]]

def bfs(i, j, plant):
    visited[i][j] = True
    region = set([(i, j)])
    q = deque([(i, j)])
    
    while q:
        cur_i, cur_j = q.popleft()
        for dir in dirs:
            new_i, new_j = cur_i + dir[0], cur_j + dir[1]
            if not in_bounds(new_i, new_j) or visited[new_i][new_j] or input[new_i][new_j] != plant or (new_i, new_j) in region:
                continue
            visited[new_i][new_j] = True
            region.add((new_i, new_j))
            q.append((new_i, new_j))
            
    regions.append(region)

def sides(region):
    corners_candidates = set()
    
    for i, j in region:
        for dir in corner_dirs:
            new_i, new_j = i + dir[0], j + dir[1]
            corners_candidates.add((new_i, new_j))
            
    corners = 0
    
    for i, j in corners_candidates:
        cells_of_corner = []
        for dir in corner_dirs:
            cells_of_corner.append((i + dir[0], j + dir[1]) in region)
            
        cells_number = sum(cells_of_corner)
        if cells_number == 1:
            corners += 1
        elif cells_number == 2:
            if cells_of_corner == [True, False, True, False] or cells_of_corner == [False, True, False, True]:
                corners += 2
        elif cells_number == 3:
            corners += 1
    
    return corners

res = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            bfs(i, j, input[i][j])

for region in regions:
    res += len(region) * sides(region)
    
print(res)