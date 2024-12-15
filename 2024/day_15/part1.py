file = open(r"2024\day_15\input.txt", "r")
map_and_moves = file.read().split('\n\n')

map_str = [line for line in map_and_moves[0].split('\n')]
moves_str = [line for line in map_and_moves[1].split('\n')]

rows, cols = len(map_str), len(map_str[0])

map = [['.'] * cols for _ in range(rows)]
moves = []

r, c = -1, -1

for i in range(rows):
    for j in range(cols):
        if map_str[i][j] == '@':
            r, c = i, j
        map[i][j] = map_str[i][j]

for i in range(len(moves_str)):
    for j in range(len(moves_str[0])):
        moves.append(moves_str[i][j])
        
dirs_map = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}
        
for move in moves:
    dir = dirs_map[move]
    has_obstacle = True
    
    if map[r + dir[0]][c + dir[1]] == '.':
        has_obstacle = False
        
    cur_r, cur_c = r, c
    while map[cur_r + dir[0]][cur_c + dir[1]] == 'O':
        cur_r += dir[0]
        cur_c += dir[1]
        
    if map[cur_r + dir[0]][cur_c + dir[1]] == '.':
        map[r][c] = '.'
        map[r + dir[0]][c + dir[1]] = '@'
        if has_obstacle:
            map[cur_r + dir[0]][cur_c + dir[1]] = 'O'
        r += dir[0]
        c += dir[1]
        
res = 0

for i in range(rows):
    for j in range(cols):
        if map[i][j] == 'O':
            res += 100 * i + j
            
print(res)