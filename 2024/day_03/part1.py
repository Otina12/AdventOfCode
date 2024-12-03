import re

file = open(r"2024\Day_03\input.txt", "r")
input = file.read()

res = 0
pattern = r'mul\([0-9]*,[0-9]*\)'

found = re.findall(pattern, input)

for mul in found:
    split_mul = re.split(r'[(,)]+', mul)
    res += int(split_mul[1]) * int(split_mul[2])
    
print(res)