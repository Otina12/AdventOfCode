file = open(r"2024\Day_06\input.txt", "r")
input = [list(line.strip()) for line in file.readlines()]

rows, cols = len(input), len(input[0])
start_i, start_j = 0, 0

for i in range(rows):
    for j in range(cols):
        if input[i][j] == '^':
            start_i, start_j = i, j
            break

def solve():
    # 0 - up, 1 - right, 2 - down, 3 - left
    cur_dir = 0
    cur_move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = set()
    visited_with_dir = set()
    i, j = start_i, start_j
    
    def in_bounds(x, y):
        return x >= 0 and x < rows and y >= 0 and y < cols

    while in_bounds(i, j):
        if (i, j, cur_dir) in visited_with_dir:
            return 1
        
        visited_with_dir.add((i, j, cur_dir))
        
        if input[i][j] == '#':
            i -= cur_move[cur_dir][0]
            j -= cur_move[cur_dir][1]
            cur_dir = (cur_dir + 1) % 4
        else:
            visited.add((i, j))
            i += cur_move[cur_dir][0]
            j += cur_move[cur_dir][1]
            
    return 0
            
res = 0
            
for x in range(rows):
    for y in range(cols):
        if input[x][y] == '.':
            input[x][y] = '#'
            res += solve()
            input[x][y] = '.'

print(res)