from collections import deque


file = open(r"2024\Day_07\input.txt", "r")
input = [line.strip() for line in file.readlines()]

test_values = []
numbers = []

for line in input:
    val, nums = line.split(': ')
    test_values.append(int(val))
    numbers.append([int(num) for num in nums.split(' ')])
    
res = 0
    
for line_i in range(len(input)):
    q = deque([numbers[line_i][0]])
    cur_j = 1
    
    while cur_j < len(numbers[line_i]):
        for i in range(len(q)):
            num = q.popleft()
            if num > test_values[line_i]:
                continue
            q.append(num + numbers[line_i][cur_j])
            q.append(num * numbers[line_i][cur_j])
            q.append(num * 10 ** len(str(numbers[line_i][cur_j])) + numbers[line_i][cur_j])
        cur_j += 1
    
    if test_values[line_i] in q:
        res += test_values[line_i]

print(res)