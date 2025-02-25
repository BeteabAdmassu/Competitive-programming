# Problem: C - Happy Partitioning - https://codeforces.com/gym/590201/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()

    p0= [0]*(n+1)
    p1 = [0]*(n+1)
    for i in range(n):
        p0[i+1] = p0[i] + (1 if a[i] == '0' else 0)
        p1[i+1] = p1[i] + (1 if a[i] == '1' else 0)

    valid_positions = []
    for i in range(n+1):
        left_count = i
        right_count = n - i
        need_left = (left_count + 1) // 2
        need_right = (right_count + 1) // 2
        if p0[i] >= need_left and (p1[n] - p1[i]) >= need_right:
            valid_positions.append(i)

    best_pos = min(valid_positions, key=lambda x: (abs(x - n / 2), x))
    print(best_pos)
