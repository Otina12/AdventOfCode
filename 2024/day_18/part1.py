from collections import deque

file = open(r"2024\day_18\input.txt", "r")
unsafe_bytes = file.read().split('\n')

rows, cols = 71, 71
num_bytes = 1024

def in_bounds(x, y):
    return x >= 0 and x < rows and y >= 0 and y < cols

memory = [['.'] * cols for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(num_bytes):
    x, y = unsafe_bytes[i].split(',')
    memory[int(y)][int(x)] = '#'

res = -1
q = deque([(0, 0, 0)])
visited[0][0] = True

while q:
    i, j, steps = q.popleft()
    
    if i == rows - 1 and j == cols - 1:
        res = steps
        break
    
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if in_bounds(new_i, new_j) and not visited[new_i][new_j] and memory[new_i][new_j] == '.':
            visited[new_i][new_j] = True
            q.append((new_i, new_j, steps + 1))

print(res)