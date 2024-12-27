from collections import deque
import math

codes = []

with open(r'2024\day_21\input.txt', 'r') as file:
    codes = [line.strip() for line in file.readlines()]

number_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['N', '0', 'A']]
arrow_keypad = [['N', '^', 'A'], ['<', 'v', '>']]
moves = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}

num_robots = 2
paths = {}
memo = {}

def num_to_pad_indeces(num):
    if num == '0':
        return [3, 1]
    elif num == 'A':
        return [3, 2]
    
    num = int(num)
    return [3 - math.ceil(num / 3), (num + 2) % 3]

def arrow_to_pad_indeces(arrow):
    match (arrow):
        case '^': return [0, 1]
        case 'A': return [0, 2]
        case '<': return [1, 0]
        case 'v': return [1, 1]
        case '>': return [1, 2]

def precompute_paths(x, y):
    i, j = arrow_to_pad_indeces(x)
    q = deque([(i, j, '')])
    paths = []

    while q:
        found = False
        
        for _ in range(len(q)):
            ci, cj, path = q.popleft()
            if arrow_keypad[ci][cj] == y:
                paths.append(path + 'A')
                found = True
                continue
            
            for move in moves.keys():
                ni, nj = ci + moves[move][0], cj + moves[move][1]
                if ni < 0 or ni >= len(arrow_keypad) or nj < 0 or nj >= len(arrow_keypad[0]) or arrow_keypad[ni][nj] == 'N':
                    continue
                q.append((ni, nj, path + move))
                
        if found:
            break

    return paths

def solve(x, y, level):
    if level == num_robots - 1:
        return len(paths[(x, y)][0])
    
    if (x, y, level) in memo:
        return memo[(x, y, level)]
    
    res_path_cost = float('inf')
    
    for path in paths[(x, y)]:
        new_path = 'A' + path
        cur_path_cost = 0
    
        for i in range(1, len(new_path)):
            cur_path_cost += solve(new_path[i-1], new_path[i], level + 1)
            
        res_path_cost = min(res_path_cost, cur_path_cost)
    
    memo[(x, y, level)] = res_path_cost
    return res_path_cost
        
def num_keypad(code):
    cur_combinations = ['']
    
    for k in range(1, len(code)):
        i, j = num_to_pad_indeces(code[k-1])
        q = deque([(i, j, '')])
        
        while q:
            paths = []
            found = False
            for _ in range(len(q)):
                ci, cj, path = q.popleft()
                if number_keypad[ci][cj] == code[k]:
                    found = True
                    paths.append(path)
                    continue
                
                for move in moves.keys():
                    ni, nj = ci + moves[move][0], cj + moves[move][1]
                    if ni < 0 or ni > 3 or nj < 0 or nj > 2 or number_keypad[ni][nj] == 'N':
                        continue
                    q.append((ni, nj, path + move))
                    
            if found:
                new_combinations = []
                for prev in cur_combinations:
                    for cur in paths:
                        new_combinations.append(prev + cur + 'A')
                cur_combinations = new_combinations
                break
            
    return cur_combinations

for a in 'A^>v<':
    for b in 'A^>v<':
        paths[(a, b)] = precompute_paths(a, b)

res = 0

for code in codes:
    combs = num_keypad('A' + code)
    
    min_cost = float('inf')
    for comb in combs:
        new_comb = 'A' + comb
        cur_cost = 0
        
        for i in range(1, len(new_comb)):
            cur_cost += solve(new_comb[i-1], new_comb[i], 0)
            
        min_cost = min(min_cost, cur_cost)
    
    res += min_cost * int(code[0:3])

print(res)