file = open(r"2024\day_17\input.txt", "r")
registers_and_input = file.read().split('\n\n')

registers_str = [line.strip() for line in registers_and_input[0].split('\n')]
input_str = registers_and_input[1].split(' ')[1].strip()

registers = []
input = []

for line in registers_str:
    registers.append(int(line.split(' ')[2]))
    
input = [int(num) for num in input_str.split(',')]

registers[0], registers[1], registers[2]

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
            registers[0] //= 2 ** combo_operand
        case 1:
            registers[1] ^= literal_operand
        case 2:
            registers[1] = combo_operand % 8
        case 3:
            if registers[0] != 0:
                i = literal_operand
                return True
        case 4:
            registers[1] ^= registers[2]
        case 5:
            res += str(combo_operand % 8) + ','
        case 6:
            registers[1] = registers[0] // 2 ** combo_operand
        case 7:
            registers[2] = registers[0] // 2 ** combo_operand
            
    return False

while i < len(input):
    opcode = input[i]
    operand = input[i+1]
    jump = operation(opcode, operand)
    
    if not jump:
        i += 2

print(f'A = {registers[0]}')
print(f'B = {registers[1]}')
print(f'C = {registers[2]}')

res = res.removesuffix(',')
print(res)