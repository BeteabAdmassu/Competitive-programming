# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

# example below, replace it with your solution
n, m = map(int, input().split())
degrees = [0] * (n + 1) 

for _ in range(m):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1

is_regular = True
if n >= 1:
    first_degree = degrees[1] if n >= 1 else 0
    for degree in degrees[2:n+1]:
        if degree != first_degree:
            is_regular = False
            break

print("YES" if is_regular else "NO")
