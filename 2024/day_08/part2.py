from collections import defaultdict

file = open(r"2024\Day_08\input.txt", "r")
input = [list(line.strip()) for line in file.readlines()]

antennas = defaultdict(list)
rows, cols = len(input), len(input[0])

for i in range(rows):
    for j in range(cols):
        if input[i][j] != '.' and input[i][j] != '#':
            antennas[input[i][j]].append((i, j))
            
def in_bounds(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols

antibodies = set()

for antenna, locations in antennas.items():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            di, dj = abs(locations[i][0] - locations[j][0]), abs(locations[i][1] - locations[j][1])
            j_dir = 1 if locations[i][1] > locations[j][1] else -1
            
            p1, p2 = locations[i][0], locations[i][1]
            while in_bounds(p1, p2):
                antibodies.add((p1, p2))
                p1 -= di
                p2 += j_dir * dj
                    
            p1, p2 = locations[j][0], locations[j][1]
            while in_bounds(p1, p2):
                antibodies.add((p1, p2))
                p1 += di
                p2 -= j_dir * dj
                
print(len(antibodies))