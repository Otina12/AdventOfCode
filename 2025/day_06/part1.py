nums = []
operations = []

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    nums = [[int(x.strip()) for x in line.split()] for line in lines[:-1]]
    operations = lines[-1].split()

n = len(nums)
m = len(operations)
res = 0

for j in range(m):
    transformed_nums = [nums[i][j] for i in range(n)]

    if operations[j] == "+":
        current_total = 0
        for num in transformed_nums:
            current_total += int(num)
    else:
        current_total = 1
        for num in transformed_nums:
            current_total *= int(num)

    res += current_total

print(res)