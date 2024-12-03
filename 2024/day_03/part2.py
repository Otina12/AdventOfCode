import re

file = open(r"2024\Day_03\input.txt", "r")
input = file.read()

res = 0
pattern = r'(mul\([0-9]*,[0-9]*\))|(do\(\))|(don\'t\(\))'

found = re.findall(pattern, input)
do = True

for patt in found:
    if len(patt[0]) > 0: # mul(x, y)
        if do:
            split_mul = re.split(r'[(,)]+', patt[0])
            res += int(split_mul[1]) * int(split_mul[2])
    elif len(patt[1]) > 0: # do()
        do = True
    elif len(patt[2]) > 0: # don't()
        do = False
    
print(res)