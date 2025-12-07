puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [[c for c in list(line.strip())] for line in file.readlines()]

rows = len(puzzle_input)
cols = len(puzzle_input[0])
memo = {}

def in_bounds(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols

def dfs(i, j):
    if not in_bounds(i, j):
        return 0
    if i == rows - 1:
        return 1
    if (i, j) in memo:
        return memo[(i, j)]
    
    puzzle_input[i][j] = '|'
    cnt = 0

    if puzzle_input[i+1][j] == '.':
        cnt = dfs(i + 1, j)
    elif puzzle_input[i+1][j] == '^':
        cnt += dfs(i + 1, j - 1)
        cnt += dfs(i + 1, j + 1)
        
    puzzle_input[i][j] = '.'
    memo[(i, j)] = cnt
    return cnt

start_point = next([i, j] for i, row in enumerate(puzzle_input) for j, c in enumerate(row) if c == 'S')

res = dfs(start_point[0], start_point[1])
print(res)