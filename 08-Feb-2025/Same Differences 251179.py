# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

t = int(input())
results = []

for _ in range(t):
    N = int(input())  
    arr = list(map(int, input().split()))
    count = 0

    freq = {}

    for i in range(N):  
        key = arr[i] - (i + 1)  
        count += freq.get(key, 0) 
        freq[key] = freq.get(key, 0) + 1  

    results.append(str(count))

print("\n".join(results))