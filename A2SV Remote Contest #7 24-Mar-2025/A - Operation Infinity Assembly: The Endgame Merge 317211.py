# Problem: A - Operation Infinity Assembly: The Endgame Merge - https://codeforces.com/gym/596004/problem/A

t = int(input())

for _ in range(t):
    n,m,k = map(int,input().split())

    a = list(input())
    b = list(input())

    a.sort()
    b.sort()

    c = []

    num_a = 0
    num_b = 0

    i = 0
    j = 0

    while i < n and j < m:
        if (a[i] < b[j] and num_a < k) or num_b >= k:
            c.append(a[i])
            i += 1
            num_a += 1
            num_b = 0
        else:
            c.append(b[j])
            j += 1
            num_b += 1
            num_a = 0

    print("".join(c))
    

