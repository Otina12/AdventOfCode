from collections import deque

file = open(r"2024\day_18\input.txt", "r")
unsafe_bytes = file.read().split('\n')

for i in range(len(unsafe_bytes)):
    x, y = unsafe_bytes[i].split(',')
    unsafe_bytes[i] = (int(y), int(x))

rows, cols = 71, 71

def in_bounds(x, y):
    return x >= 0 and x < rows and y >= 0 and y < cols

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(n):
    memory = [['.'] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]

    for i in range(n):
        memory[unsafe_bytes[i][0]][unsafe_bytes[i][1]] = '#'
    
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        i, j = q.popleft()
        
        if i == rows - 1 and j == cols - 1:
            return True
        
        for dir in dirs:
            new_i, new_j = i + dir[0], j + dir[1]
            if in_bounds(new_i, new_j) and not visited[new_i][new_j] and memory[new_i][new_j] == '.':
                visited[new_i][new_j] = True
                q.append((new_i, new_j))
                
    return False

l, r = 0, len(unsafe_bytes) - 1

while l < r:
    m = (l + r) // 2
    
    if bfs(m + 1):
        l = m + 1
    else:
        r = m

res = f'{unsafe_bytes[l][1]},{unsafe_bytes[l][0]}'
print(res)