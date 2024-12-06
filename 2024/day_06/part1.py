file = open(r"2024\Day_06\input.txt", "r")
input = [line.strip() for line in file.readlines()]

rows, cols = len(input), len(input[0])
start_i, start_j = 0, 0

for i in range(rows):
    for j in range(cols):
        if input[i][j] == '^':
            start_i, start_j = i, j
            break

# 0 - up, 1 - right, 2 - down, 3 - left
cur_dir = 0
cur_move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
visited = set()
i, j = start_i, start_j

def in_bounds(x, y):
    return x >= 0 and x < rows and y >= 0 and y < cols

while in_bounds(i, j):
    if input[i][j] == '#':
        i -= cur_move[cur_dir][0]
        j -= cur_move[cur_dir][1]
        cur_dir = (cur_dir + 1) % 4
    else:
        visited.add((i, j))
        i += cur_move[cur_dir][0]
        j += cur_move[cur_dir][1]

print(len(visited))