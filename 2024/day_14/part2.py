import re
import matplotlib.pyplot as plt

file = open(r"2024\day_14\input.txt", "r")
input = [line.strip() for line in file.readlines()]

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
robots = []

for line in input:
    x, y, dx, dy = map(int, re.search(pattern, line).groups())
    robots.append([x, y, dx, dy])

rows, cols = 103, 101
arr = [['.'] * cols for _ in range(rows)]

def max_connected_component(arr):
    positions = set((y, x) for x, y, _, _ in arr)
    visited = [[False] * cols for _ in range(rows)]
    res = 0
    
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) not in positions or visited[i][j]:
            return 0
        
        visited[i][j] = True
        return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
        
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and (i, j) in positions:
                cluster_size = dfs(i, j)
                res = max(res, cluster_size)
                
    return res
                
def show_robots():
    grid = [[[0, 0, 0] for _ in range(cols)] for _ in range(rows)]
    
    for x, y, _, _ in robots:
        grid[y][x] = [0, 255, 0]

    plt.imshow(grid)
    plt.show()

seconds = 0

while True:
    seconds += 1
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % cols
        robot[1] = (robot[1] + robot[3]) % rows
    
    if max_connected_component(robots) > 100:
        show_robots()
        break
    
print(seconds)