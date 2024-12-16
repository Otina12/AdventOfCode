file = open(r"2024\day_12\input.txt", "r")
input = [list(line.strip()) for line in file.readlines()]

rows, cols = len(input), len(input[0])
            
def in_bounds(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols

visited = [[False] * cols for _ in range(rows)]
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(i, j, plant):
    if not in_bounds(i, j) or input[i][j] != plant:
        return (0, 1)
    if visited[i][j]:
        return (0, 0)
    
    visited[i][j] = True
    area = 1
    perimeter = 0
    
    for dir in dirs:
        temp = dfs(i + dir[0], j + dir[1], plant)
        area += temp[0]
        perimeter += temp[1]
        
    return (area, perimeter)

res = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            area_and_perimeter = dfs(i, j, input[i][j])
            res += area_and_perimeter[0] * area_and_perimeter[1]
            
print(res)