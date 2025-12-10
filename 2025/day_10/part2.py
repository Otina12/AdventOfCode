import re
import pulp

joltages = []
button_groups = []

with open("input.txt", "r") as file:
    for line in file:
        jolts_part = re.search(r'\{([^}]*)\}', line)
        jolts = [int(x) for x in jolts_part.group(1).split(',')]
        size = len(jolts)
        
        buttons_part = re.findall(r'\(([^)]*)\)', line)
        group_bits = []
        for group in buttons_part:
            nums = [int(x) for x in group.split(',')]
            bit_list = [1 if i in nums else 0 for i in range(size)]
            group_bits.append(bit_list)

        joltages.append(jolts)
        button_groups.append(group_bits)

def solve_machine(joltage_target, buttons):
    m = len(joltage_target)
    k = len(buttons)

    problem = pulp.LpProblem('machine', pulp.LpMinimize)
    x = [pulp.LpVariable(f"x_{j}", lowBound = 0, cat = 'Integer') for j in range(k)]
    problem += pulp.lpSum(x)

    for i in range(m):
        problem += pulp.lpSum(buttons[j][i] * x[j] for j in range(k)) == joltage_target[i]

    problem.solve(pulp.PULP_CBC_CMD(msg = False))
    presses = sum(int(press.value()) for press in x)
    return presses

n = len(joltages)
res = 0 

for i in range(n):
    res += solve_machine(joltages[i], button_groups[i])

print(res)