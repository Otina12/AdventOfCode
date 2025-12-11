from collections import defaultdict

outgoing_devices = defaultdict(list)

with open("input.txt", "r") as file:
    for line in file:
        device_parts = line.split(':')
        input_device = device_parts[0]
        output_devices = device_parts[1].strip().split(' ')

        outgoing_devices[input_device] = output_devices

memo = {}

def dfs(src, destination):
    if src == destination:
        return 1
    if src in memo:
        return memo[src]
    
    total_ways = 0
    for outgoing_device in outgoing_devices[src]:
        total_ways += dfs(outgoing_device, destination)

    memo[src] = total_ways
    return total_ways

starting_device = 'you'
ending_device = 'out'

res = dfs(starting_device, ending_device)
print(res)