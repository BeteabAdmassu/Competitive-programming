# Problem: A - Harmonic Melody - https://codeforces.com/gym/590201/problem/A

N = int(input())


for _ in range(N):
    M = int(input())

    notes =  list(map(int, input().split()))


    perfect = True
    for i in range(len(notes) - 1):
        interval = abs(notes[i] - notes[i + 1])
        if interval not in {5, 7}:
            perfect = False
            break
    print("YES" if perfect else "NO")