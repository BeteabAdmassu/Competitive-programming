# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = []
x, y = 0, 0
for i in range(5):
    matrix.append(list(map(int, input().split())))
    for j in range(5):
        if matrix[i][j] == 1:
            x, y = i, j
if x > 2:
    x = x - 2
else: 
    x = 2 - x
if y > 2:
    y = y -2
else:
    y = 2 - y
print(x+y)