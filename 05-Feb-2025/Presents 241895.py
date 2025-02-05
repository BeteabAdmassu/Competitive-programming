# Problem: Presents - https://codeforces.com/problemset/problem/136/A

import copy
N = int(input())
array = [0] * N

arr = input().split(" ")
t = arr.copy()

for i in range(len(arr)):
    arr[int(t[i]) - 1] = i + 1

output = " ".join(map(str,arr))

print(output)