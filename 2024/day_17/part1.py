file = open(r"2024\day_17\input.txt", "r")
registers_and_input = file.read().split('\n\n')

registers_str = [line.strip() for line in registers_and_input[0].split('\n')]
input_str = registers_and_input[1].split(' ')[1].strip()

registers = []
input = []

for line in registers_str:
    registers.append(int(line.split(' ')[2]))
    
input = [int(num) for num in input_str.split(',')]

A = registers[0]
B = registers[1]
C = registers[2]

res = ''
i = 0

def operation(opcode, operand):
    global i
    global res

    literal_operand = operand
    combo_operand = operand
    
    if operand > 3 and operand != 7:
        combo_operand = registers[operand - 4]
        
    match opcode:
        case 0:
            A //= 2 ** combo_operand
        case 1:
            B ^= literal_operand
        case 2:
            B = combo_operand % 8
        case 3:
            if A != 0:
                i = literal_operand
                return True
        case 4:
            B ^= C
        case 5:
            res += str(combo_operand % 8) + ','
        case 6:
            B = A // 2 ** combo_operand
        case 7:
            C = A // 2 ** combo_operand
            
    return False

while i < len(input):
    opcode = input[i]
    operand = input[i+1]
    jump = operation(opcode, operand)
    
    if not jump:
        i += 2

print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')

res = res.removesuffix(',')
print(res)