file = open(r"2024\Day_07\input.txt", "r")
input = [line.strip() for line in file.readlines()]

test_values = []
numbers = []

for line in input:
    val, nums = line.split(': ')
    test_values.append(int(val))
    numbers.append([int(num) for num in nums.split(' ')])
    
true_equations = set()
    
def solve(line_i, i, cur_res):
    if cur_res > test_values[line_i]:
        return
    if i == len(numbers[line_i]):
        if cur_res == test_values[line_i]:
            true_equations.add(line_i)
        return
    
    solve(line_i, i + 1, cur_res + numbers[line_i][i])
    solve(line_i, i + 1, cur_res * numbers[line_i][i])
    solve(line_i, i + 1, cur_res * 10 ** len(str(numbers[line_i][i])) + numbers[line_i][i])
    
for line_i in range(len(input)):
    solve(line_i, 1, numbers[line_i][0])
    
res = 0

for line_i in true_equations:
    res += test_values[line_i]
    
print(res)