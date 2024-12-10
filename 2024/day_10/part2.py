from collections import defaultdict

file = open(r"2024\day_10\input.txt", "r")
input = [[int(d) for d in line.strip()] for line in file.readlines()]

rows, cols = len(input), len(input[0])
            
def in_bounds(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols

def dfs(i, j, cur_height):
    if not in_bounds(i, j) or input[i][j] != cur_height:
        return 0
    
    if input[i][j] == 9:
        return 1
    
    return (dfs(i+1, j, cur_height + 1) +
            dfs(i-1, j, cur_height + 1) +
            dfs(i, j+1, cur_height + 1) +
            dfs(i, j-1, cur_height + 1))
    
res = 0

for i in range(rows):
    for j in range(cols):
        if input[i][j] == 0:
            res += dfs(i, j, 0)

print(res)