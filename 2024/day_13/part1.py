import re

file = open(r"2024\day_13\input.txt", "r")
input = file.read().split('\n\n')

machines = []
pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

for info in input:
    ax, ay, bx, by, x, y = map(int, re.search(pattern, info).groups())
    machines.append((ax, ay, bx, by, x, y))

def solve(machine):
    ax, ay, bx, by, x, y = machine
    
    if (x * by - y * bx) % (ax * by - ay * bx) == 0:
        k = (x * by - y * bx) // (ax * by - ay * bx)
        
        if (x - ax * k) % bx == 0:
            t = (x - ax * k) // bx
            
            if 0 <= k <= 100 and 0 <= t <= 100:
                return 3 * k + t
        
    return 0

res = 0

for machine in machines:
    res += solve(machine)

print(res)