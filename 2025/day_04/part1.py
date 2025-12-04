puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [[c for c in line.strip()] for line in file.readlines()]

rows = len(puzzle_input)
cols = len(puzzle_input[0])
dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def in_bounds(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols

def get_neighbor_count(i, j):
    nei_cnt = 0

    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if in_bounds(new_i, new_j) and puzzle_input[new_i][new_j] == '@':
            nei_cnt += 1

    return nei_cnt

res = 0

for i in range(rows):
    for j in range(cols):
        if puzzle_input[i][j] == '@' and get_neighbor_count(i, j) < 4:
            res += 1

print(res)