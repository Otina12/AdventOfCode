file = open(r"2024\Day_09\input.txt", "r")
input = file.readline()

files = []
spaces = []
is_file = True
id = 0
i = 0

for c in input:
    cnt = int(c)
    
    if is_file:
        files.append((i, cnt, id))
        id += 1
    else:
        spaces.append([i, cnt])
        
    is_file = not is_file
    i += cnt

def sum(start, end):
    return end * (end - 1) // 2 - start * (start - 1) // 2

res = 0

for j in range(len(files)):
    i, cnt, id = files[j]
    res += sum(i, i + cnt) * id

for j in range(len(files) - 1, -1, -1):
    i, cnt, id = files[j]
    p_i = 0
    
    while p_i < len(spaces) and spaces[p_i][0] < i and cnt > spaces[p_i][1]:
        p_i += 1
        
    if p_i == len(spaces) or spaces[p_i][0] >= i:
        continue
    else:
        start, end = spaces[p_i][0], spaces[p_i][0] + cnt
        res -= sum(i, i + cnt) * id
        res += sum(start, end) * id
        
        spaces[p_i][0] += cnt
        spaces[p_i][1] -= cnt
        
print(res)