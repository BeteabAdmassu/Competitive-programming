# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
matrix = []
for _ in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)

if n == 1:
    print(max(matrix[0]))
    exit()

dp = [[0] * len(matrix[0]) for _ in range(n)]

dp[0] = matrix[0]

for i in range(n):
    for j in range(len(matrix[0])):
        if j == 0:
            dp[i][j] = max(dp[i - 1][j + 1], dp[i - 1][j + 2]) + matrix[i][j]
        elif j == 1:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j + 1]) + matrix[i][j]
        elif j == 2:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j - 2]) + matrix[i][j]

print(max(dp[n-1]))