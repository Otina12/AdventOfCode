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
    if (src, destination) in memo:
        return memo[(src, destination)]
    
    total_ways = 0
    for outgoing_device in outgoing_devices[src]:
        total_ways += dfs(outgoing_device, destination)

    memo[(src, destination)] = total_ways
    return total_ways

starting_device = 'svr'
dac_device = 'dac'
fft_device = 'fft'
ending_device = 'out'

res = 0
res += dfs(starting_device, fft_device) * dfs(fft_device, dac_device) * dfs(dac_device, ending_device) # svr -> fft -> dac -> out
res += dfs(starting_device, dac_device) * dfs(dac_device, fft_device) * dfs(fft_device, ending_device) # svr -> dac -> fft -> out

print(res)