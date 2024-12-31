secret_nums = []

with open(r'2024\day_22\input.txt', 'r') as file:
    secret_nums = [int(line.strip()) for line in file.readlines()]
    
total_steps = 2000
mask = (1 << 24) - 1

def mix(num1, num2):
    return num1 ^ num2

def prune(num):
    return num & mask

def last_secret_num(num):
    for _ in range(total_steps):
        num = prune(mix(num, num << 6))
        num = prune(mix(num, num >> 5))
        num = prune(mix(num, num << 11))
    
    return num

res = 0

for secret_num in secret_nums:
    res += last_secret_num(secret_num)

print(res)