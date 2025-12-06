puzzle_input = []

with open("input.txt", "r") as file:
    puzzle_input = [line for line in file.readlines()]

    for i in range(len(puzzle_input) - 1):
        puzzle_input[i] = puzzle_input[i][:-1]

def transpose(arr):
    n, m = len(arr), len(arr[0])
    transposed = [[''] * n for _ in range(m)]

    for j in range(m):
        for i in range(n):
            transposed[j][i] = arr[i][j]

    return transposed

def split_by_blank_rows(arr):
    groups = []
    current = []

    for row in arr:
        if all(c == ' ' for c in row):
            if current:
                groups.append(current)
                current = []
        else:
            current.append(''.join(row))

    groups.append(current)
    return groups

def parse_expression(expression_arr):
    nums = []
    operation = None

    for i, expr in enumerate(expression_arr):
        if '+' in expr:
            operation = '+'
            expression_arr[i] = expr.replace('+', '')
        elif '*' in expr:
            operation = '*'
            expression_arr[i] = expr.replace('*', '')
        
        nums.append(int(expression_arr[i].replace(' ', '')))

    return operation, nums

puzzle_input = split_by_blank_rows(transpose(puzzle_input))
res = 0

for expression_arr in puzzle_input:
    operation, nums = parse_expression(expression_arr)

    if operation == "+":
        current_total = 0
        for num in nums:
            current_total += int(num)
    else:
        current_total = 1
        for num in nums:
            current_total *= int(num)

    res += current_total

print(res)