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
    next = set(ordering)
        
    for i in range(1, len(update)):
        for j in range(i):
            if (update[i], update[j]) in next:
                return False
            
    return True

res = 0

for update in updates:
    if is_ordered(ordering, update):
        res += update[len(update) // 2]
    
print(res)