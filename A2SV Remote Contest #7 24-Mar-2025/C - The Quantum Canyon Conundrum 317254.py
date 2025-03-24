# Problem: C - The Quantum Canyon Conundrum - https://codeforces.com/gym/596004/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    compressed = [arr[0]]
    for x in arr[1:]:
        if x != compressed[-1]:
            compressed.append(x)
    
    c = 0
    for i in range(len(compressed)):
        left_greater = (i == 0) or (compressed[i-1] > compressed[i])
        right_greater = (i == len(compressed) - 1) or (compressed[i+1] > compressed[i])
        if left_greater and right_greater:
            c += 1

    print("YES" if c == 1 else "NO")