file = open(r"2024\Day_09\input.txt", "r")
input = file.readline()

files = []
is_file = True
id = 0

for d in input:
    cnt = int(d)
    
    if is_file:
        files += cnt * [id]
        id += 1
    else:
        files += cnt * [-1]
        
    is_file = not is_file

res = 0

for i in range(len(files)):
    if files[i] != -1:
        res += i * files[i]

i, j = 0, len(files) - 1

while i < j:
    while files[i] != -1:
        i += 1
    while files[j] == -1:
        j -= 1
    
    if i < j:
        res -= j * files[j]
        res += i * files[j]
        
    i += 1
    j -= 1
        
print(res)