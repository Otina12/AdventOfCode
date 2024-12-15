file = open(r"2024\day_15\input.txt", "r")
map_and_moves = file.read().split('\n\n')

map_str = [line for line in map_and_moves[0].split('\n')]
moves_str = [line for line in map_and_moves[1].split('\n')]

rows, old_cols = len(map_str), len(map_str[0])
cols = old_cols * 2

map = [['.'] * cols for _ in range(rows)]
moves = []

r, c = -1, -1

for i in range(rows):
    for j in range(old_cols):
        if map_str[i][j] == '@':
            r, c = i, 2 * j
            map[i][2*j] = '@'
            map[i][2*j+1] = '.'
        elif map_str[i][j] == 'O':
            map[i][2*j] = '['
            map[i][2*j+1] = ']'
        else:
            map[i][2*j] = map_str[i][j]
            map[i][2*j+1] = map_str[i][j]

for i in range(len(moves_str)):
    for j in range(len(moves_str[0])):
        moves.append(moves_str[i][j])
        
dirs_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
def can_move_boxes(i, j, dir):
    if map[i + dir[0]][j] == '#':
        return False
    elif map[i + dir[0]][j] == '.':
        return True
    
    can = can_move_boxes(i + dir[0], j, dir)
    
    if not can:
        return False
    
    if map[i + dir[0]][j] == ']':
        can &= can_move_boxes(i + dir[0], j - 1, dir)
    else: # [
        can &= can_move_boxes(i + dir[0], j + 1, dir)
        
    return can
    
def move_boxes(i, j, dir):
    if map[i + dir[0]][j] == '.':
        map[i + dir[0]][j] = map[i][j]
        map[i][j] = '.'
        return

    move_boxes(i + dir[0], j, dir)
    new_j = j - 1 if map[i + 2 * dir[0]][j] == ']' else j + 1 # + 2 * dir[0] because it's already moved
    move_boxes(i + dir[0], new_j, dir)
    
    map[i + dir[0]][j] = map[i][j]
    map[i][j] = '.'

for move in moves:
    dir_i = dirs_map[move]
    dir = dirs[dir_i]
    
    if dir_i % 2 == 1: # horizontal move
        cur_c = c
        while map[r][cur_c + dir[1]] in '[]':
            cur_c += dir[1]
        if map[r][cur_c + dir[1]] == '.':
            while cur_c != c:
                map[r][cur_c + dir[1]] = map[r][cur_c]
                cur_c -= dir[1]
            
            map[r][c] = '.'
            map[r][c + dir[1]] = '@'
            c += dir[1]
    else: # vertical move
        if can_move_boxes(r, c, dir):
            move_boxes(r, c, dir)
            map[r][c] = '.'
            map[r + dir[0]][c + dir[1]] = '@'
            r += dir[0]
            c += dir[1]
            
res = 0

for i in range(rows):
    for j in range(cols):
        if map[i][j] == '[':
            res += 100 * i + j
            
print(res)