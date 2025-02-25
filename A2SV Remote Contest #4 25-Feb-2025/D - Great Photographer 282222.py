# Problem: D - Great Photographer - https://codeforces.com/gym/590201/problem/D

n, x0 = map(int, input().split())
segments = []
for _ in range(n):
    a, b = map(int, input().split())
    segments.append([a, b])

left_values = []
right_values = []
for segment in segments:
    left_values.append(min(segment[0], segment[1]))
    right_values.append(max(segment[0], segment[1]))
left = max(left_values)
right = min(right_values)

if left > right:
    print(-1)  
elif left <= x0 <= right:
    print(0) 
else:
    print(min(abs(x0 - left), abs(x0 - right)))