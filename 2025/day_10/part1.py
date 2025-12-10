import re

machines = []
button_groups = []

with open("input.txt", "r") as file:
    for line in file:
        machine_part = re.search(r'\[([.#]+)\]', line).group(1)
        machine_bits = ''.join('1' if c == '#' else '0' for c in machine_part)
        size = len(machine_bits)

        buttons_part = re.findall(r'\(([^)]*)\)', line)
        button_group = []
        for group in buttons_part:
            nums = [int(x) for x in group.split(',')]
            button_bit_str = ''.join('1' if i in nums else '0' for i in range(size))
            button_group.append(button_bit_str)

        machines.append(machine_bits)
        button_groups.append(button_group)

def is_bit_set(num, i):
    return (num & (1 << i)) != 0

def is_valid(machine_str, buttons_strs, combination):
    machine = int(machine_str, 2)
    buttons = [int(b, 2) for b in buttons_strs]

    limit = combination.bit_length()
    res_machine = 0

    for i in range(limit):
        if is_bit_set(combination, i):
            res_machine ^= buttons[i]

    return res_machine == machine

n = len(machines)
res = 0

for i in range(n):
    machine = machines[i]
    buttons = button_groups[i]

    cnt = len(buttons)
    min_buttons = float('inf')

    for combination in range(1 << cnt):
        if is_valid(machine, buttons, combination):
            min_buttons = min(min_buttons, combination.bit_count())
    
    res += min_buttons

print(res)
