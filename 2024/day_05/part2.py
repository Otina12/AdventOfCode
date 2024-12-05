from collections import defaultdict

file = open(r"2024\Day_05\input.txt", "r")
input = file.read()
    
ordering, updates = input.split('\n\n')
ordering = ordering.split('\n')
updates = updates.split('\n')

for i in range(len(ordering)):
    x, y = ordering[i].split('|')
    ordering[i] = (int(x), int(y))
    
for i in range(len(updates)):
    updates[i] = [int(x) for x in updates[i].split(',')]
    
ordering = set(ordering)

def is_ordered(update):
    for i in range(1, len(update)):
        for j in range(i):
            if (update[i], update[j]) in ordering:
                return False
            
    return True

def order(update):
    while True:
        is_sorted = True
        for i in range(len(update) - 1):
            if (update[i+1], update[i]) in ordering:
                is_sorted = False
                update[i], update[i+1] = update[i+1], update[i]
            
        if is_sorted:
            return update

res = 0

for update in updates:
    if is_ordered(update):
        continue
    order(update)
    res += update[len(update) // 2]

print(res)