file = open(r"2024\Day_01\input.txt", "r")
list1, list2 = [], []

for line in file:
    locs = line.split('   ')
    list1.append(int(locs[0]))
    list2.append(int(locs[1]))
    
list1.sort()
list2.sort()

diff = 0

for i in range(len(list1)):
    diff += abs(list1[i] - list2[i])
    
print(diff)