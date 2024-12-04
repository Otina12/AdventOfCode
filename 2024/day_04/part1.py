file = open(r"2024\Day_04\input.txt", "r")
input = []

for line in file:
    input.append(line.strip())

def search(word, arr):
    m, n = len(arr), len(arr[0])
    dirs = [[0, 1], [1, 0], [1, 1], [1, -1]]
    res = 0
    
    def checkWord(i, j, dir):
        ni, nj = i, j
        
        for k in range(4):
            if ni < 0 or ni >= m or nj < 0 or nj >= n or arr[ni][nj] != word[k]:
                return 0
            ni += dir[0]
            nj += dir[1]
            
        return 1
   
    for i in range(m):
        for j in range(n):
            if arr[i][j] == word[0]: # to reduce number of function calls
                for dir in dirs:
                    res += checkWord(i, j, dir)
    
    return res

print(search('XMAS', input) + search('SAMX', input))