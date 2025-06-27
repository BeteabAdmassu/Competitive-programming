# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

# example below, replace it with your solution
n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

sources = []
sinks = []

for i in range(n):
    is_source = True
    for j in range(n):
        if adj_matrix[j][i] == 1:
            is_source = False
            break
    if is_source:
        sources.append(i + 1)  

for i in range(n):
    is_sink = True
    for j in range(n):
        if adj_matrix[i][j] == 1:
            is_sink = False
            break
    if is_sink:
        sinks.append(i + 1)  # vertices are 1-based in output

print(len(sources), end=' ')
print(' '.join(map(str, sorted(sources))))
print(len(sinks), end=' ')
print(' '.join(map(str, sorted(sinks))))
