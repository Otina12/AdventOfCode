file = open(r"2024\day_19\input.txt", "r")
input = file.read().split('\n\n')

patterns = [line for line in input[0].split(', ')]
designs = [line for line in input[1].split('\n')]

patterns = set(patterns)
max_pattern_len = max([len(p) for p in patterns])
memo = {}

def is_possible(design_i, i):
    if i == len(designs[design_i]):
        return True
    
    if (design_i, i) in memo:
        return memo[(design_i, i)]
    
    ans = False
    
    for k in range(1, max_pattern_len + 1):
        if designs[design_i][i:i+k] in patterns:
            ans |= is_possible(design_i, i + k)
            
    memo[(design_i, i)] = ans
    return ans

res = 0

for des_i in range(len(designs)):
    if is_possible(des_i, 0):
        res += 1

print(res)