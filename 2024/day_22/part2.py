from collections import defaultdict

secret_nums = []

with open(r'2024\day_22\input.txt', 'r') as file:
    secret_nums = [int(line.strip()) for line in file.readlines()]

n = len(secret_nums)
total_steps = 2000
mask = (1 << 24) - 1
buyer_prices = defaultdict(int)

def mix(num1, num2):
    return num1 ^ num2

def prune(num):
    return num & mask

def solve(num):
    price_changes = []
    cur_price = num % 10
    seen = set()
    
    for _ in range(total_steps):
        num = prune(mix(num, num << 6))
        num = prune(mix(num, num >> 5))
        num = prune(mix(num, num << 11))
        
        next_price = num % 10
        change = next_price - cur_price
        price_changes.append(change)
        cur_price = next_price
        
        m = len(price_changes)
        if m > 3:
            k = (price_changes[m-4], price_changes[m-3], price_changes[m-2], price_changes[m-1])
            if k in seen:
                continue
            seen.add(k)
            buyer_prices[k] += cur_price
            
for num in secret_nums:
    solve(num)

res = max(buyer_prices.values())
print(res)