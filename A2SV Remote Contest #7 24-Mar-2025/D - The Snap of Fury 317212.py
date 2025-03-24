# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

n = int(input())
claw_lengths = list(map(int, input().split()))

attack_intervals = []
for i in range(n):
    start = max(0, i - claw_lengths[i])
    end = i - 1
    if start <= end:
        attack_intervals.append((start, end))

attack_intervals.sort()
merged_intervals = []

for start, end in attack_intervals:
    if not merged_intervals:
        merged_intervals.append((start, end))
    else:
        last_start, last_end = merged_intervals[-1]
        if start <= last_end:
            merged_intervals[-1] = (last_start, max(end, last_end))
        else:
            merged_intervals.append((start, end))

killed_creatures = 0
for start, end in merged_intervals:
    killed_creatures += (end - start + 1)

print(n - killed_creatures)
