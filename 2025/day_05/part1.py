id_intervals = []
available_ids = []

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

    blank_line_idx = lines.index("")

    for interval in lines[:blank_line_idx]:
        start, end = interval.split("-")
        id_intervals.append((int(start), int(end)))

    for x in lines[blank_line_idx + 1:]:
        available_ids.append(int(x))

def merge_intervals(intervals):
    intervals.sort(key = lambda x : x[0])
    merged_intervals = []

    cur_start, cur_end = id_intervals[0][0], id_intervals[0][1]

    for i in range(1, len(id_intervals)):
        interval = id_intervals[i]

        if interval[0] > cur_end:
            merged_intervals.append((cur_start, cur_end))
            cur_start, cur_end = interval[0], interval[1]
        else:
            cur_end = max(cur_end, interval[1])

    merged_intervals.append((cur_start, cur_end))
    return merged_intervals

def exists_in_interval_bs(intervals, target):
    left, right = 0, len(intervals) - 1

    while left <= right:
        mid = left + (right - left) // 2
        start, end = intervals[mid]

        if target < start:
            right = mid - 1
        elif target > end:
            left = mid + 1
        else:
            return True

    return False

id_intervals = merge_intervals(id_intervals)
res = 0

for id in available_ids:
    if exists_in_interval_bs(id_intervals, id):
        res += 1

print(res)