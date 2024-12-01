from collections import defaultdict

file = open(r"2024\Day_01\input.txt", "r")
list1 = []
list2 = defaultdict(int)

for line in file:
    locs = line.split('   ')
    list1.append(int(locs[0]))
    list2[int(locs[1])] += 1

res = 0

for loc in list1:
    res += loc * list2[loc]
    
print(res)