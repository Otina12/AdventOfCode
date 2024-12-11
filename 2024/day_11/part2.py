file = open(r"2024\day_11\input.txt", "r")
input = [int(num) for num in file.readline().split(' ')]

blink_times = 75
cur_stones = input
memo = {}
res = 0

def solve(stone, step):
    if step == blink_times:
        return 1
    
    if (stone, step) in memo:
        return memo[(stone, step)]
    
    memo[(stone, step)] = 0
    digit_number = len(str(stone))
    
    if stone == 0:
        memo[(stone, step)] += solve(1, step + 1)
    elif digit_number & 1 == 0:
        memo[(stone, step)] += solve(int(str(stone)[0:digit_number // 2]), step + 1) + solve(int(str(stone)[digit_number // 2:]), step + 1)
    else:
        memo[(stone, step)] += solve(stone * 2024, step + 1)
    
    return memo[(stone, step)]

for cur_stone in cur_stones:
    res += solve(cur_stone, 0)

print(res)