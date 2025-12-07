puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [[c for c in list(line.strip())] for line in file.readlines()]

rows = len(puzzle_input)
cols = len(puzzle_input[0])

def in_bounds(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols

def split_count(i, j):
    if not in_bounds(i, j):
        return 0
    if puzzle_input[i][j] == '|':
        return 0
    
    puzzle_input[i][j] = '|'

    if i == rows - 1:
        return 0
    if puzzle_input[i+1][j] == '.':
        return split_count(i + 1, j)
    if puzzle_input[i+1][j] == '^':
        return 1 + split_count(i + 1, j - 1) + split_count(i + 1, j + 1)
    
    return 0

start_point = next([i, j] for i, row in enumerate(puzzle_input) for j, c in enumerate(row) if c == 'S')

res = split_count(start_point[0], start_point[1])
print(res)