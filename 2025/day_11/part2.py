from collections import defaultdict

outgoing_devices = defaultdict(list)

with open("input.txt", "r") as file:
    for line in file:
        device_parts = line.split(':')
        input_device = device_parts[0]
        output_devices = device_parts[1].strip().split(' ')

        outgoing_devices[input_device] = output_devices

memo = {}

def dfs(src, destination, visited_dac, visited_fft):
    if src == destination and visited_dac and visited_fft:
        return 1

    key = (src, visited_dac, visited_fft)
    if key in memo:
        return memo[key]

    total_ways = 0
    for outgoing_device in outgoing_devices[src]:
        new_visited_dac = visited_dac or (outgoing_device == dac_device)
        new_visited_fft = visited_fft or (outgoing_device == fft_device)
        total_ways += dfs(outgoing_device, destination, new_visited_dac, new_visited_fft)

    memo[key] = total_ways
    return total_ways

starting_device = 'svr'
dac_device = 'dac'
fft_device = 'fft'
ending_device = 'out'

res = dfs(starting_device, ending_device, False, False)
print(res)