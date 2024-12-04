file = open(r"2024\Day_04\input.txt", "r")
input = []

for line in file:
    input.append(line.strip())

word = 'MAS'

m, n = len(input), len(input[0])
res = 0

def checkWord(i, j):
    if i < 1 or i > m - 2 or j < 1 or j > n - 2:
        return 0
    
    first_diagonal = input[i-1][j-1] == word[0] and input[i+1][j+1] == word[2] or input[i-1][j-1] == word[2] and input[i+1][j+1] == word[0]
    second_diagonal = input[i-1][j+1] == word[0] and input[i+1][j-1] == word[2] or input[i-1][j+1] == word[2] and input[i+1][j-1] == word[0]
    
    return int(first_diagonal and second_diagonal)

for i in range(m):
    for j in range(n):
        if input[i][j] == word[1]: # to reduce number of function calls
            res += checkWord(i, j)

print(res)