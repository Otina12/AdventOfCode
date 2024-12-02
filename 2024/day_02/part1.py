file = open(r"2024\Day_02\input.txt", "r")
input = []
res = 0

def is_valid(arr):
    incr = arr[1] > arr[0]
    
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) > 3:
            return False
        if incr and arr[i] <= arr[i-1] or not incr and arr[i] >= arr[i-1]:
            return False
            
    return True

for line in file:
    arr = [int(num) for num in line.split(' ')]
    
    if is_valid(arr):
        res += 1
        
print(res)
