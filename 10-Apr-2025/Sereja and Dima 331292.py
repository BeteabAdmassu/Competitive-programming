# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())

cards = list(map(int, input().split()))


left, right = 0, n - 1
sereja = 0
dima = 0
for i in range(n):
    if i % 2 == 0:
        if cards[left] > cards[right]:
            sereja += cards[left]
            left += 1
        else:
            sereja += cards[right]
            right -= 1
    else:
        if cards[left] > cards[right]:
            dima += cards[left]
            left += 1
        else:
            dima += cards[right]
            right -= 1
print(sereja, dima)